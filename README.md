# spackr
additional/custom R packages for spack, e.g., 

- [x] TMB
- [ ] INLA
- [ ] eppasm
- [ ] naomi

## How to:

clone this repo to, for example, `spackr`, then edit the default repos 
located at
`etc/spack/defaults/repos.yaml`, changing from

```yaml
repos:
- $spack/var/spack/repos/builtin
```

to

```yaml
repos:
- ~/spackr
- $spack/var/spack/repos/builtin
```

