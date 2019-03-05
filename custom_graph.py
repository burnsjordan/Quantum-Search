from quantum_search import apply_circuit
import matplotlib.pyplot as plt
import sys

def vary_coefficients(t,a,b,c,d,alpha,applications):
    a_results = []
    b_results = []
    c_results = []
    d_results = []
    x_a = []
    x_b = []
    x_c = []
    x_d = []

    for i in range(10):
        a_results.append(apply_circuit(t,i*0.1*a,b,c,d,alpha,applications))
        b_results.append(apply_circuit(t,a,i*0.1*b,c,d,alpha,applications))
        c_results.append(apply_circuit(t,a,b,i*0.1*c,d,alpha,applications))
        d_results.append(apply_circuit(t,a,b,c,i*0.1*d,alpha,applications))
        x_a.append(i*0.1*a)
        x_b.append(i*0.1*b)
        x_c.append(i*0.1*c)
        x_d.append(i*0.1*d)

    # Print result
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
    ax1.plot(x_a,a_results)
    ax1.set_ylabel('Probability')
    ax1.set_xlabel('a')
    ax1.set_title('A Results')
    ax2.plot(x_b,b_results)
    ax2.set_ylabel('Probability')
    ax2.set_xlabel('b')
    ax2.set_title('B Results')
    ax3.plot(x_c,c_results)
    ax3.set_ylabel('Probability')
    ax3.set_xlabel('c')
    ax3.set_title('C Results')
    ax4.plot(x_d,d_results)
    ax4.set_ylabel('Probability')
    ax4.set_xlabel('d')
    ax4.set_title('D Results')
    plt.ylabel('Probability')
    plt.show()

def vary_time(t,a,b,c,d,alpha,applications):
    results = []
    x = []
    for i in range(10):
        results.append(apply_circuit(t*0.1*i,a,b,c,d,alpha,applications))
        x.append(i*0.1*t)
    plt.plot(x,results)
    plt.ylabel('Probability')
    plt.xlabel('Time')
    plt.show()

def vary_alpha(t,a,b,c,d,alpha,applications):
    results = []
    x = []
    for i in range(10):
        results.append(apply_circuit(t,a,b,c,d,alpha*0.1*i,applications))
        x.append(i*0.1*alpha)
    plt.plot(x,results)
    plt.ylabel('Probability')
    plt.xlabel('Alpha')
    plt.show()

def vary_applications(t,a,b,c,d,alpha,applications):
    results = []
    x = []
    for i in range(applications):
        results.append(apply_circuit(t,a,b,c,d,alpha,i))
        x.append(i)
    plt.plot(x,results)
    plt.ylabel('Probability')
    plt.xlabel('Applications')
    plt.show()

if (str(sys.argv[1])=='coefficients'):
    vary_coefficients(float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]),float(sys.argv[7]),int(sys.argv[8]))
elif (str(sys.argv[1])=='time'):
    vary_time(float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]),float(sys.argv[7]),int(sys.argv[8]))
elif (str(sys.argv[1])=='alpha'):
    vary_alpha(float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]),float(sys.argv[7]),int(sys.argv[8]))
elif (str(sys.argv[1])=='applications'):
    vary_applications(float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]),float(sys.argv[7]),int(sys.argv[8]))
else:
    print('Unknown Command')
