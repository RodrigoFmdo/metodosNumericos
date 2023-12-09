-- No le hagan caso a esta cosa
metodoBiseccion :: (Double -> Double) -> Double -> Double -> Double -> Double
metodoSecanteMaxN :: (Double -> Double) -> Int -> Double -> Double -> Double
metodoSecanteErr :: (Double -> Double) -> Double -> Double -> Double -> Double

-- En haskell no existen el for o while por lo que todo está de manera recursiva pero
-- mas o menos si se pone uno de los dos en lugar del if sale lo mismo



-- El metodo de la biseccion, tiene como condicion de paro que el intervalo
-- para aproximar la raiz sea menor o igual al error
metodoBiseccion func err a b = 
    let c = (a + b) / 2
        fa = func a
        fb = func b
        fc = func c
    in
        if b-a <= err then c 
        else if fa * fc < 0  then metodoBiseccion func err a c 
        else metodoBiseccion func err c b 

-- En este metodo de la secante tiene como forma de para un maximo numero de iteraciones
-- o que fb - fa sea 0. Esto para evitar dividir sobre este
metodoSecanteMaxN func maxN a b =
    if maxN > 1 then 
        let fa = func a 
            fb = func b
            c = b - fb * (b - a) / (fb - fa)
        in 
            if fb - fa == 0 then b
            else metodoSecanteMaxN func (maxN-1) b c
    else b

-- La condicion de paro igual es fb - fa = 0 o c-b < err
metodoSecanteErr func err a b = 
    let fa = func a
        fb = func b 
        c = b - fb * (b - a) / (fb - fa)
    in 
        if fb - fa == 0 || abs (c - b) < err then b
        else metodoSecanteErr func err b c

-- Para el metodo de la secante hay un algoritmo en el libro pero al chile no me gusto
-- se complica de mas la vida y para nada
