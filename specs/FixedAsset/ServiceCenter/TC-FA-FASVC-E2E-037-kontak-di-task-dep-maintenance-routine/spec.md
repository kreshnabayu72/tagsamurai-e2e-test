---
id: TC-FA-FASVC-E2E-037-kontak-di-task-dep-maintenance-routine
title: "Kontak Service Center di Task: Nama Kontak Primary, Telepon, Email, dan Nilai Kosong"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FASVC-LOGIC-08c, "§9.7#r13", "§2.2#r3", "§Aturan Logika Modul#p6", EC-FASVC-42c]
smoke: []
dependsOn: ["Maintenance Routine: Task"]
trace:
  FASVC-LOGIC-08c: [2, 3, 4, 5, 22, 23, 24, 25]
  "§9.7#r13": 35
  "§2.2#r3": [2, 22]
  "§Aturan Logika Modul#p6": [3, 4, 5, 6, 8, 9, 11, 12, 14, 15, 16, 18, 19, 41, 42]
  EC-FASVC-42c: [36, 37]
anchor: []
coverage:
  web: automated
---

# Kontak Service Center di Task: Nama Kontak Primary, Telepon, Email, dan Nilai Kosong

## Prerequisites
- Aktor: Staff `Eko Saputra {runId}`. Aktor lain: Approver `Fajar Nugroho {runId}` dan Total Control (mengubah kontak dan membuka pemilih).
- Layar awal: Maintenance Routine, daftar Task milik aktor.
- Data:
  - DU-037-1: Group `Cabang Kontak {runId}`.
  - DU-037-2: User `Eko Saputra {runId}`, Role Staff, cakupan Group `Cabang Kontak {runId}`; ditugaskan pada Task DU-037-9 sampai DU-037-13.
  - DU-037-3: User `Fajar Nugroho {runId}`, Role Approver, cakupan Group `Cabang Kontak {runId}`; penyetuju Task DU-037-14.
  - DU-037-4: Service Center `Teknik Kontak Lengkap {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Kontak {runId}`, City `Surabaya`, Company phone `+62 215550201`, Company email `info@kontaklengkap.example`; Primary: Agus Prasetyo {runId}, phone +62 81234567801, email agus@kontaklengkap.example; Bukan Primary: Bagas Wibowo {runId}, phone +62 81234567802, email bagas@kontaklengkap.example.
  - DU-037-5: Service Center `Teknik Kontak Email Saja {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Kontak {runId}`, City `Surabaya`, Company phone `+62 215550202`, Company email `info@kontakemail.example`; Primary: Citra Lestari {runId}, phone kosong, email citra@kontakemail.example.
  - DU-037-6: Service Center `Teknik Kontak Telepon Saja {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Kontak {runId}`, City `Surabaya`, Company phone `+62 215550203`, Company email `info@kontaktelepon.example`; Primary: Dedi Kurniawan {runId}, phone +62 81234567803, email kosong.
  - DU-037-7: Service Center `Teknik Tanpa Kontak {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Kontak {runId}`, City `Surabaya`, Company phone `+62 215550204`, Company email `—`; tanpa Contact persons.
  - DU-037-8: Service Center `Teknik Tanpa Telepon {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Kontak {runId}`, City `Jakarta`, Company phone `—`, Company email `info@tanpatelepon.example`; tanpa Contact persons.
  - DU-037-9: Task aset `Kompresor Kontak Satu {runId}`, Group `Cabang Kontak {runId}`, Status `To Do`, pelaksana `Teknik Kontak Lengkap {runId}`.
  - DU-037-10: Task aset `Pompa Kontak Dua {runId}`, Group `Cabang Kontak {runId}`, Status `To Do`, pelaksana `Teknik Kontak Email Saja {runId}`.
  - DU-037-11: Task aset `Mesin Kontak Tiga {runId}`, Group `Cabang Kontak {runId}`, Status `To Do`, pelaksana `Teknik Kontak Telepon Saja {runId}`.
  - DU-037-12: Task aset `Genset Kontak Empat {runId}`, Group `Cabang Kontak {runId}`, Status `To Do`, pelaksana `Teknik Tanpa Kontak {runId}`.
  - DU-037-13: Task aset `Boiler Kontak Lima {runId}`, Group `Cabang Kontak {runId}`, Status `To Do`, pelaksana `Teknik Tanpa Telepon {runId}`.
  - DU-037-14: Task aset `Chiller Kontak Enam {runId}`, Group `Cabang Kontak {runId}`, Status `Waiting for Approval`, pelaksana `Teknik Kontak Lengkap {runId}`.
- Kondisi:
  - Lisensi addon Maintenance aktif.
  - Akun Staff, Approver, dan Total Control aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Kontak Primary tampil di Task Staff
1. Buka Task aset `Kompresor Kontak Satu {runId}` di Maintenance Routine
2. Verifikasi nama Service Center `Teknik Kontak Lengkap {runId}` tampil di Task
3. Verifikasi nama kontak Primary `Agus Prasetyo {runId}` tampil
4. Verifikasi telepon `+62 81234567801` dari kontak Primary tampil
5. Verifikasi email `agus@kontaklengkap.example` dari kontak Primary tampil
6. Verifikasi kontak `Bagas Wibowo {runId}` yang bukan Primary tidak tampil

### Telepon dan email kosong pada kontak Primary diganti nilai perusahaan
7. Buka Task aset `Pompa Kontak Dua {runId}` di Maintenance Routine
8. Verifikasi telepon `+62 215550202` dari Company phone tampil, karena kontak Primary `Citra Lestari {runId}` tanpa telepon
9. Verifikasi email `citra@kontakemail.example` dari kontak Primary tampil
10. Buka Task aset `Mesin Kontak Tiga {runId}` di Maintenance Routine
11. Verifikasi telepon `+62 81234567803` dari kontak Primary `Dedi Kurniawan {runId}` tampil
12. Verifikasi email `info@kontaktelepon.example` dari Company email tampil, karena kontak Primary tanpa email

### Tanpa kontak Primary dan nilai perusahaan kosong tampil sebagai strip
13. Buka Task aset `Genset Kontak Empat {runId}` di Maintenance Routine
14. Verifikasi nama kontak Primary tampil `—`
15. Verifikasi telepon `+62 215550204` dari Company phone tampil
16. Verifikasi email tampil `—`
17. Buka Task aset `Boiler Kontak Lima {runId}` di Maintenance Routine
18. Verifikasi telepon tampil `—`
19. Verifikasi email `info@tanpatelepon.example` dari Company email tampil

### Kontak Service Center tampil di Task Approver
20. Masuk sebagai Approver `Fajar Nugroho {runId}`
21. Buka Task aset `Chiller Kontak Enam {runId}` di Maintenance Routine
22. Verifikasi nama Service Center `Teknik Kontak Lengkap {runId}` tampil di Task
23. Verifikasi nama kontak Primary `Agus Prasetyo {runId}` tampil
24. Verifikasi telepon `+62 81234567801` dari kontak Primary tampil
25. Verifikasi email `agus@kontaklengkap.example` dari kontak Primary tampil

### Perubahan kontak langsung tampil di Task
26. Masuk sebagai Total Control
27. Buka Add-ons > Service Center
28. Ketik Search `Teknik Kontak Lengkap {runId}`, tekan Enter
29. Klik `⋯` pada baris `Teknik Kontak Lengkap {runId}`
30. Klik `Edit`
31. Ganti Phone kontak Primary `Agus Prasetyo {runId}` dengan Dial Code `+62` dan nomor `81234567899`
32. Klik `[Save]`
33. Masuk sebagai Staff `Eko Saputra {runId}`
34. Buka Task aset `Kompresor Kontak Satu {runId}` di Maintenance Routine
35. Verifikasi telepon `+62 81234567899` dari kontak Primary terkini tampil

### Staff tidak memiliki menu Service Center tetapi nama dan kontak tetap tampil di Task
36. Verifikasi menu `Add-ons > Service Center` tidak tampil di navigasi Staff
37. Verifikasi nama kontak Primary `Agus Prasetyo {runId}` tetap tampil di Task

### Opsi pemilih memuat Name, City, dan Company phone
38. Masuk sebagai Total Control
39. Buka Task aset `Kompresor Kontak Satu {runId}` di Maintenance Routine
40. Klik pemilih `Select service center` pada Task itu
41. Verifikasi opsi `Teknik Kontak Lengkap {runId} · Surabaya · +62 215550201` tampil
42. Verifikasi opsi `Teknik Tanpa Telepon {runId} · Jakarta · —` tampil
