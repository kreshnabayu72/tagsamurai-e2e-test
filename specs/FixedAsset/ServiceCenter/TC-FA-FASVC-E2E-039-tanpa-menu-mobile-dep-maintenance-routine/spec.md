---
id: TC-FA-FASVC-E2E-039-tanpa-menu-mobile-dep-maintenance-routine
title: "Aplikasi Mobile: Tanpa Menu Service Center, Kontak di Task Dapat Ditekan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.6#p1"]
smoke: []
dependsOn: ["Maintenance Routine: Task"]
trace:
  "§4.6#p1": [3, 5, 6, 7, 9, 10, 11]
anchor: [2]
coverage:
  android: manual
---

# Aplikasi Mobile: Tanpa Menu Service Center, Kontak di Task Dapat Ditekan

## Prerequisites
- Aktor: Staff `Joko Susilo {runId}` di aplikasi mobile Android.
- Layar awal: Aplikasi mobile Android, daftar Task milik aktor.
- Data:
  - DU-039-1: Group `Cabang Seluler {runId}`.
  - DU-039-2: User `Joko Susilo {runId}`, Role Staff, cakupan Group `Cabang Seluler {runId}`; ditugaskan pada Task DU-039-4 dan DU-039-6.
  - DU-039-3: Service Center `Teknik Seluler Mandiri {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Seluler {runId}`, City `Denpasar`, Company phone `+62 361550301`, Company email `info@teknikseluler.example`; Contact persons: Primary `Wayan Sudarma {runId}`, phone `+62 81234567830`, email `wayan@teknikseluler.example`.
  - DU-039-4: Task aset `Kompresor Seluler {runId}`, Status `To Do`, pelaksana `Teknik Seluler Mandiri {runId}`.
  - DU-039-5: Service Center `Mitra Seluler Tanpa Kontak {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Seluler {runId}`, City `Denpasar`, Company phone `+62 361550302`, tanpa Company email, tanpa contact person.
  - DU-039-6: Task aset `Genset Seluler {runId}`, Status `To Do`, pelaksana `Mitra Seluler Tanpa Kontak {runId}`.
- Kondisi:
  - Lisensi addon Maintenance aktif.
  - Akun Staff aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Aplikasi mobile tidak memiliki menu Service Center
1. Buka menu navigasi aplikasi mobile
2. Verifikasi navigasi aplikasi mobile memuat menu selain `Service Center`
3. Verifikasi menu `Service Center` tidak tersedia di navigasi aplikasi mobile

### Kontak Service Center di Task mobile dapat ditekan
4. Buka Task aset `Kompresor Seluler {runId}` di aplikasi mobile
5. Verifikasi nama kontak Primary `Wayan Sudarma {runId}` tampil di Task
6. Verifikasi telepon `+62 81234567830` tampil dan dapat ditekan
7. Verifikasi email `wayan@teknikseluler.example` tampil dan dapat ditekan

### Kontak Service Center tanpa contact person di Task mobile: nilai yang ada dapat ditekan, yang kosong tidak
8. Buka Task aset `Genset Seluler {runId}` di aplikasi mobile
9. Verifikasi nama kontak Primary tampil `—`
10. Verifikasi telepon `+62 361550302` dari Company phone tampil dan dapat ditekan
11. Verifikasi email tampil `—` dan tidak dapat ditekan
