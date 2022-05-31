package edu.princeton.cs.algs4;

/**
 *  The {@code Arbitrage} class provides a client that finds an arbitrage
 *  opportunity in a currency exchange table by constructing a
 *  complete-digraph representation of the exchange table and then finding
 *  a negative cycle in the digraph.
 *  <p>
 *  This implementation uses the Bellman-Ford algorithm to find a
 *  negative cycle in the complete digraph.
 *  The running time is proportional to <em>V</em><sup>3</sup> in the
 *  worst case, where <em>V</em> is the number of currencies.
 *  <p>
 *  This code is guaranteed to find an arbitrage opportunity in a 
 *  currency exchange table (or report that no such arbitrage 
 *  opportunity exists) under the assumption that all arithmetic
 *  performed is without floating-point rounding error or arithmetic
 *  overflow. Since the code computes the logarithms of the edge weights,
 *  floating-point rounding error will be present and it may fail on
 *  some pathological inputs.
 *  <p>
public class Arbitrage {

    // this class cannot be instantiated
    private Arbitrage() { }

    /**
     *  Reads the currency exchange table from standard input and
     *  prints an arbitrage opportunity to standard output (if one exists).
     *
     * @param args the command-line arguments
     */
    public static void main(String[] args) {

        // V currencies
        int V = StdIn.readInt();
        String[] name = new String[V];

        // create complete network
        EdgeWeightedDigraph G = new EdgeWeightedDigraph(V);
        for (int v = 0; v < V; v++) {
            name[v] = StdIn.readString();
            for (int w = 0; w < V; w++) {
                double rate = StdIn.readDouble();
                DirectedEdge e = new DirectedEdge(v, w, -Math.log(rate));
                G.addEdge(e);
            }
        }

        // find negative cycle
        BellmanFordSP spt = new BellmanFordSP(G, 0);
        if (spt.hasNegativeCycle()) {
            double stake = 1000.0;
            for (DirectedEdge e : spt.negativeCycle()) {
                StdOut.printf("%10.5f %s ", stake, name[e.from()]);
                stake *= Math.exp(-e.weight());
                StdOut.printf("= %10.5f %s\n", stake, name[e.to()]);
            }
        }
        else {
            StdOut.println("No arbitrage opportunity");
        }
    }

}

 *  algs4.jar is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
