#ifndef COSTROMEOTORQUE_H
#define COSTROMEOTORQUE_H

#include "costfunction.h"

class CostRomeoTorque : public CostFunction<double,4,1>
{
public:
    CostRomeoTorque();
private:
    stateMat_t Q;
    commandMat_t R;
    double dt;
protected:
    // attributes //
public:
private:

protected:
    // methods //
public:
    void computeAllCostDeriv(const stateVec_t& X,const stateVec_t& Xdes, const commandVec_t& U);
    void computeFinalCostDeriv(const stateVec_t& X,const stateVec_t& Xdes);
private:
protected:
    // accessors //
public:

};

#endif // COSTROMEOTORQUE_H
