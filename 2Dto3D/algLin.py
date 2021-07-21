import numpy as np 

Rot_X = lambda theta    : np.array([[ 1, 0            ,  0            , 0 ],
                                    [ 0, np.cos(theta), -np.sin(theta), 0 ],
                                    [ 0, np.sin(theta),  np.cos(theta), 0 ],
                                    [ 0, 0            ,  0            , 1 ]])

Rot_Y = lambda theta    : np.array([[ np.cos(theta), 0, np.sin(theta), 0],
                                    [ 0            , 1, 0            , 0],
                                    [-np.sin(theta), 0, np.cos(theta), 0],
                                    [ 0            , 0,             0, 1]])

Rot_Z = lambda theta    : np.array([[ np.cos(theta), -np.sin(theta), 0, 0],
                                    [ np.sin(theta),  np.cos(theta), 0, 0],
                                    [ 0            ,  0            , 1, 0],
                                    [ 0            ,  0            , 0, 1]])
 
Trans_X = lambda dx     : np.array([[ 1, 0, 0, dx ],
                                    [ 0, 1, 0, 0  ],
                                    [ 0, 0, 1, 0  ],
                                    [ 0, 0, 0, 1  ]])

Trans_Y = lambda dy     : np.array([[ 1, 0, 0, 0  ],
                                    [ 0, 1, 0, dy ],
                                    [ 0, 0, 1, 0  ],
                                    [ 0, 0, 0, 1  ]])

Trans_Z = lambda dz     : np.array([[ 1, 0, 0, 0  ],
                                    [ 0, 1, 0, 0  ],
                                    [ 0, 0, 1, dz ],
                                    [ 0, 0, 0, 1  ]])

Trans = lambda dx,dy,dz : np.array([[ 1, 0, 0, dx ],
                                    [ 0, 1, 0, dy ],
                                    [ 0, 0, 1, dz ],
                                    [ 0, 0, 0, 1  ]])

