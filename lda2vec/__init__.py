import lda2vec.dirichlet_likelihood as dirichlet_likelihood
import lda2vec.embed_mixture as embed_mixture
import lda2vec.tracking as tracking 
import lda2vec.preprocess as preprocess
import lda2vec.corpus as corpus
import lda2vec.topics as topics
import lda2vec.negative_sampling as negative_sampling

dirichlet_likelihood = dirichlet_likelihood.dirichlet_likelihood
EmbedMixture = embed_mixture.EmbedMixture
Tracking = tracking.Tracking
tokenize = preprocess.tokenize
Corpus = corpus.Corpus
prepare_topics = topics.prepare_topics
print_top_words_per_topic = topics.print_top_words_per_topic
negative_sampling = negative_sampling.negative_sampling
topic_coherence = topics.topic_coherence
