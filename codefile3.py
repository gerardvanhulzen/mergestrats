#parse the command line arguments
print("Parsing the arguments")
parser = argparse.ArgumentParser()
parser.add_argument("-s","--source",help="pass the sourcefile to be read")
parser.add_argument("-nf","--nodes_filename",help="pass the nodes CSV filename")
parser.add_argument("-ef","--edges_filename",help="pass the edges CSV filename")

args = parser.parse_args()
log_file = args.source
nodes_file = args.nodes_filename
edges_file = args.edges_filename

#run the program
main(log_file,nodes_file,edges_file)
