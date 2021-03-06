from setup import tc, rm, get_sandbox_path

import logging
logger = logging.getLogger(__name__)

def test_random_forest_regressor(tc):

    logger.info("define schema")
    schema = [("Class", int),("Dim_1", float),("Dim_2", float)]

    logger.info("creating the frame")
    data = [[1,19.8446136104,2.2985856384],
            [1,16.8973559126,2.6933495054],
            [1,5.5548729596,2.7777687995],
            [0,46.1810010826,3.1611961917],
            [0,44.3117586448,3.3458963222],
            [0,34.6334526911,3.6429838715],
            [1,11.4849647497,3.8530199663],
            [0,43.7438430327,3.9347590844],
            [0,44.961185029,4.0953872464],
            [0,37.0549734365,4.1039157849],
            [0,52.0093009461,4.1455433148],
            [0,38.6092023162,4.1615595686],
            [0,33.8789730794,4.1970765922],
            [1,-1.0388754777,4.4190319518],
            [0,49.913080358,4.5445142439],
            [1,3.2789270744,4.8419490458],
            [1,9.7921007601,4.8870605498],
            [0,45.5778621825,4.9665753213],
            [0,45.4773893261,5.0764210643],
            [0,44.303211041,5.1112029237],
            [0,52.8429742116,5.4121654741],
            [1,14.8057269164,5.5634291719],
            [0,42.6043814342,5.5988383751],
            [1,13.7291123825,5.6684973484],
            [0,50.7410573499,5.6901229975],
            [0,52.0093990181,5.7401924186]]

    f = tc.frame.create(data, schema=schema)
    logger.info(f.inspect())

    logger.info("training the model on the frame")
    model = tc.models.regression.random_forest_regressor.train(f, 'Class', ['Dim_1', 'Dim_2'])
    logger.info("predicting the class using the model and the frame")
    model.predict(f)
    assert(set(f.column_names) == set(['Class', 'Dim_1', 'Dim_2','predicted_value']))
    assert(len(f.column_names) == 4)
