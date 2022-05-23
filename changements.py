x = 250
i = np.nonzero(ax == x)[0][0]
trace_x = gpanel[:,i]
#plt.plot(at,trace_x)
i_max = np.argmax(trace_x)
t_max = at[i_max]

print(f"le maximum du sinus cardinal est atteint en t_max = {t_max.round(2)}")
print(f"parametres: tf - {tf}, nt - {nt}")
def error(a): 
   S = 0
   for k in range(0,nt):
      t = k*tf/nt
      if np.abs(t-t_max) < 0.08:
         S += (trace_x[k] - np.sinc(a*(t-t_max)))**2
   return S

error = np.vectorize(error)
fig, axes = plt.subplots(3, figsize = (6,20))
fig.suptitle('Détermination du meilleur coefficient a')
axes[0].plot(np.linspace(0.1,100,200), error(np.linspace(0.1,100,200)))
axes[1].plot(np.linspace(27,31,100),error(np.linspace(27,31,100)) )
axes[2].plot(np.linspace(29,29.6,100),error(np.linspace(29,29.6,100)) )
for i in range(3):
   axes[i].set(xlabel = "a (en Hz)", ylabel = "erreur")

print("l'erreur atteint son minimum pour a = 29.4 s-1 environ")
   