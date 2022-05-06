import matplotlib.pyplot as plt

t=[0,1,2,3,4,5,6,7,8]
bi = [1,0,1,0,1,1,1,0,0]

#Unipolar NRZ
unipolarNRZ=[]
for x in bi:
	for i in range(100):
		unipolarNRZ.append(x)
plt.title("Unipolar NRZ")
plt.plot(unipolarNRZ)
plt.show()

#Polar NRZ
polarNRZ=[]
pol=[]
i=0
for k in bi:
	if k==1:
		pol.append(k)
	else:
		pol.append(-1)
	i+=1
for x in pol:
	for i in range(100):
		polarNRZ.append(x)
plt.title("Polar NRZ")
plt.plot(polarNRZ)
plt.show()

#Polar RZ
polarRZ=[]
pol=[]
i=0
for k in bi:
	if k==1:
		pol.append(k)
	else:
		pol.append(-1)
	i+=1
for x in pol:
	for i in range(50):
		polarRZ.append(x)
	for i in range(50):
		polarRZ.append(0)
plt.title("Polar RZ")
plt.plot(polarRZ)
plt.show()

#bipolar NRZ
bipolarNRZ=[]
pol=bi
i=0
count=0
for x in pol:
	if x==1:
		if i==1:
			pol[count]=-1
			i=0
		else:
			i=1
	count+=1
for x in pol:
	for i in range(100):
		bipolarNRZ.append(x)
plt.title("Bipolar NRZ")
plt.plot(bipolarNRZ)
plt.show()

#Manchester Encoding
man=[]
pol=[]
i=0
for k in bi:
	if k==1:
		pol.append(1)
	else:
		pol.append(-1)
	i+=1
for x in pol:
	for i in range(50):
		man.append(x)
	for i in range(50):
		man.append(0)
plt.title("Manchester Encoding")
plt.plot(man)
plt.show()
t=[0,1,2,3,4,5,6,7,8]
bi = [1,0,1,0,1,1,1,0,0]

#Unipolar NRZ
unipolarNRZ=[]
for x in bi:
	for i in range(100):
		unipolarNRZ.append(x)
plt.title("Unipolar NRZ")
plt.plot(unipolarNRZ)
plt.show()

#Polar NRZ
polarNRZ=[]
pol=[]
i=0
for k in bi:
	if k==1:
		pol.append(k)
	else:
		pol.append(-1)
	i+=1
for x in pol:
	for i in range(100):
		polarNRZ.append(x)
plt.title("Polar NRZ")
plt.plot(polarNRZ)
plt.show()

#Polar RZ
polarRZ=[]
pol=[]
i=0
for k in bi:
	if k==1:
		pol.append(k)
	else:
		pol.append(-1)
	i+=1
for x in pol:
	for i in range(50):
		polarRZ.append(x)
	for i in range(50):
		polarRZ.append(0)
plt.title("Polar RZ")
plt.plot(polarRZ)
plt.show()

#bipolar NRZ
bipolarNRZ=[]
pol=bi
i=0
count=0
for x in pol:
	if x==1:
		if i==1:
			pol[count]=-1
			i=0
		else:
			i=1
	count+=1
for x in pol:
	for i in range(100):
		bipolarNRZ.append(x)
plt.title("Bipolar NRZ")
plt.plot(bipolarNRZ)
plt.show()

#Manchester Encoding
man=[]
pol=[]
i=0
for k in bi:
	if k==1:
		pol.append(1)
	else:
		pol.append(-1)
	i+=1
for x in pol:
	for i in range(50):
		man.append(x)
	for i in range(50):
		man.append(0)
plt.title("Manchester Encoding")
plt.plot(man)
plt.show()