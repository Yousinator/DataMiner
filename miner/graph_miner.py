import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st

class GraphMining:
    def __init__(self, df):
        self.df = df

    def create_graph_by_name(self, name):
        courses = self.split_certificates(name)
        rows = self.df[self.df["Name"] == name]
        print(len(rows))
        if len(rows) == 0:
            return 1
        else:
            for i, row in rows.iterrows():
                G = nx.Graph()

                for row in courses:
                    for course in row:
                        G.add_edge(name, course, weight=1)
                        break
                break

            self.plot_graph(G, name)
            return 0

    def create_graph_by_certificate(self, certificate):
        rows = self.df[self.df["Certifications"] == certificate]
        if len(rows) == 0:
            return "No Matching Certification"
        else:
            nodes = []
            edges = []
            projects = []
            for i, row in rows.iterrows():
                nodes.append(row["Certifications"])
                edges.append(row["Name"])
                projects.append(row["Project Count"])
            g = pd.DataFrame({"source": nodes, "target": edges, "weight": projects})

            Y = nx.from_pandas_edgelist(g, edge_attr="weight", create_using=nx.DiGraph())

            pos = nx.spring_layout(Y)
            nx.draw_networkx(Y, pos, with_labels=True, node_size=700)
            labels = nx.get_edge_attributes(Y, "weight")
            nx.draw_networkx_edge_labels(Y, pos, edge_labels=labels)

            plt.title(f"Graph of {certificate} Certifications")
            st.pyplot(plt)  # Use st.pyplot() instead of plt.show()

    def plot_graph(self, G, name):
        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos, with_labels=True, node_size=700)
        plt.title(f"Certificates for {name}")
        st.pyplot(plt)  # Use st.pyplot() instead of plt.show()

    def split_certificates(self, name):
        rows = self.df[self.df["Name"] == name]
        courses = rows["Programming Languages"].apply(lambda x: x.split("; "))
        return courses
