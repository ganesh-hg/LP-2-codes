{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6a4a18c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "BFS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "521cfde1",
   "metadata": {},
   "outputs": [],
   "source": [
    "graph = {\n",
    "    '5': ['3', '7'],\n",
    "    '3': ['2', '4'],\n",
    "    '7': ['8'],\n",
    "    '2': [],\n",
    "    '4': ['8'],\n",
    "    '8': []\n",
    "}\n",
    "\n",
    "visited = []\n",
    "queue = []\n",
    "\n",
    "def bfs(visited, graph, node):\n",
    "  visited.append(node)\n",
    "  queue.append(node)\n",
    "\n",
    "  while queue:\n",
    "    m = queue.pop(0)\n",
    "    print(m, end='\\n')\n",
    "\n",
    "    for neighbour in graph[m]:\n",
    "      if neighbour not in visited:\n",
    "        visited.append(neighbour)\n",
    "        queue.append(neighbour)\n",
    "\n",
    "print(\"BFS:\")\n",
    "bfs(visited, graph, '5')\n",
    "\n",
    "# Output:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "82c98a36",
   "metadata": {},
   "outputs": [],
   "source": [
    "DFS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a90b0153",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "DFS:\n",
      "5\n",
      "3\n",
      "2\n",
      "4\n",
      "8\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "graph = {\n",
    "    '5': ['3', '7'],\n",
    "    '3': ['2', '4'],\n",
    "    '7': ['8'],\n",
    "    '2': [],\n",
    "    '4': ['8'],\n",
    "    '8': []\n",
    "}\n",
    "\n",
    "visited = []\n",
    "\n",
    "def dfs(visited, graph, node):\n",
    "  if node not in visited:\n",
    "    print(node)\n",
    "    visited.append(node)\n",
    "    for neighbour in graph[node]:\n",
    "      dfs(visited, graph, neighbour)\n",
    "\n",
    "print(\"DFS:\")\n",
    "dfs(visited, graph, '5')\n",
    "\n",
    "# Output:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee015453",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
