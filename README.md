# customer_analysis
The goal of this project was to identify different types of customers in a shopping mall based on how much they earn and how much they spend. This helps businesses understand their customers better so they can send personalized offers. For example, they may want to target high spenders with loyalty programs or try to convert low spenders into active buyers.
Understanding the Data
The dataset used is the popular Mall Customer Segmentation Data, which includes:
Gender
Age
Annual Income (k$)
Spending Score (1-100)


The author mostly focused on Annual Income and Spending Score to form the clusters, as these two features are easy to visualize and highly relevant for marketing purposes.
How Clustering Works
Since this is an unsupervised learning problem, we don’t have any labels (like “high spender” or “low spender”). Instead, we use K-Means to automatically group customers with similar traits.
Before applying K-Means, we need to decide how many clusters (K) we want. The notebook used the Elbow Method, which involves plotting something called WCSS (within-cluster sum of squares). We look for the point where the plot “bends” or forms an elbow — this is usually a good value for K. In this case, K = 5 was chosen.
What I Learned from the Clusters
Once the algorithm was run, it divided the customers into five groups. Each group had similar spending and income behavior. For example:
Some customers had high income but low spending


Others had low income but high spending


And one group had both high income and high spending


This kind of analysis can be really useful for businesses. For me, it was eye-opening to see how simple clustering can uncover these patterns without any labels or supervision.
My Takeaways
This project helped me understand:
The basics of clustering and how K-Means works


How to choose the number of clusters using the Elbow Method


The importance of visualizing data to interpret results


How machine learning can solve practical business problems


I also found that even with just two features, K-Means can create meaningful customer groups. In future projects, I’d like to try adding more features (like age or gender) and maybe compare K-Means with other clustering algorithms like DBSCAN or Agglomerative Clustering.
Final Thoughts
Overall, this was a great beginner-friendly project to get hands-on with machine learning. I enjoyed not just the technical part, but also thinking about how the output can be used in real-life scenarios. If you're just starting with machine learning like me, I definitely recommend trying out this project.
