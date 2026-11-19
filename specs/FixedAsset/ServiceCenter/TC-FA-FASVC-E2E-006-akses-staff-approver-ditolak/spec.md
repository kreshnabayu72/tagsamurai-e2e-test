---
id: TC-FA-FASVC-E2E-006-akses-staff-approver-ditolak
title: "Staff dan Approver: Menu Tidak Tampil dan URL Langsung Menampilkan Empty State"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["FASVC-LOGIC-08b", "EC-FASVC-34", "EC-FASVC-42a", "EC-FASVC-42b", "F-FASVC-01.k2", "§2.1#b1", "EB-AKS-1", "EB-AKS-2", "§9.4.3#b8"]
smoke: []
dependsOn: []
trace:
  "FASVC-LOGIC-08b": [25, 31]
  "EC-FASVC-34": 27
  "EC-FASVC-42a": [25, 31]
  "EC-FASVC-42b": [27, 33]
  "F-FASVC-01.k2": [27, 33]
  "§2.1#b1": [25, 31]
  "EB-AKS-1": [3, 13, 16, 19, 22, 25, 31]
  "EB-AKS-2": [27, 33, 36]
  "§9.4.3#b8": [25, 28, 31, 34]
anchor: [24, 30]
coverage:
  web: automated
---

# Staff dan Approver: Menu Tidak Tampil dan URL Langsung Menampilkan Empty State

## Prerequisites
- Aktor: Total Control `Tania Control {runId}`, Group Manager `Gita Manager {runId}`, Asset Admin `Anisa Admin {runId}`, Monitoring & Report `Maya Monitoring {runId}`, Read Only `Rudi ReadOnly {runId}`, Staff `Sari Staff {runId}`, Approver `Anton Approver {runId}`, dan pengguna tanpa sesi login.
- Layar awal: Dashboard Fixed Asset.
- Data:
  - DU-006-1: Group `Head Office`, node root pohon Group entitas aktor.
  - DU-006-2: Group `Branch Surabaya`, anak dari `Head Office`.
  - DU-006-3: Aktor `Tania Control {runId}` dengan Role `Total Control`.
  - DU-006-4: Aktor `Gita Manager {runId}` dengan Role `Group Manager`, cakupan `Head Office`.
  - DU-006-5: Aktor `Anisa Admin {runId}` dengan Role `Asset Admin`, Role Transaksi `Maintenance Routine`, cakupan `Branch Surabaya`.
  - DU-006-6: Aktor `Maya Monitoring {runId}` dengan Role `Monitoring & Report`, Role Transaksi `Maintenance Routine`, cakupan `Branch Surabaya`.
  - DU-006-7: Aktor `Rudi ReadOnly {runId}` dengan Role `Read Only`, cakupan `Branch Surabaya`, hanya capability read.
  - DU-006-8: Aktor `Sari Staff {runId}` dengan Role `Staff`, tanpa capability di modul Service Center.
  - DU-006-9: Aktor `Anton Approver {runId}` dengan Role `Approver`, tanpa capability di modul Service Center.
  - DU-006-10: Pengguna tanpa sesi login.
  - DU-006-11: Service Center `Servis Rahasia {runId}`, Service type `Routine`, Available to `All groups`, City `Jakarta Selatan`, Company email `kontak@servisrahasia.co.id`, dibuat oleh `Tania Control {runId}`. Usage `0`.
- Kondisi:
  - Lisensi addon Maintenance aktif untuk entitas aktor.
  - Akun semua aktor aktif dan kredensialnya disediakan fase 2.
  - Master Data Count Limit bernilai `1000` dan entitas aktor berisi kurang dari 1.000 Service Center.

## Test Steps

### Total Control melihat menu dan menyiapkan Service Center sebagai pemicu
1. Masuk sebagai `Tania Control {runId}`
2. Buka menu `Add-ons` pada sidebar
3. Verifikasi menu `Service Center` tampil di bawah `Add-ons`
4. Klik `Service Center`
5. Klik `[+ Service Center]`
6. Isi Name `Servis Rahasia {runId}`
7. Centang Service type `Routine`
8. Isi City `Jakarta Selatan`
9. Isi Company email `kontak@servisrahasia.co.id`
10. Klik `[Submit]`

### Group Manager melihat menu Service Center
11. Masuk sebagai `Gita Manager {runId}`
12. Buka menu `Add-ons` pada sidebar
13. Verifikasi menu `Service Center` tampil di bawah `Add-ons`

### Asset Admin melihat menu Service Center
14. Masuk sebagai `Anisa Admin {runId}`
15. Buka menu `Add-ons` pada sidebar
16. Verifikasi menu `Service Center` tampil di bawah `Add-ons`

### Monitoring & Report melihat menu Service Center
17. Masuk sebagai `Maya Monitoring {runId}`
18. Buka menu `Add-ons` pada sidebar
19. Verifikasi menu `Service Center` tampil di bawah `Add-ons`

### Read Only melihat menu Service Center
20. Masuk sebagai `Rudi ReadOnly {runId}`
21. Buka menu `Add-ons` pada sidebar
22. Verifikasi menu `Service Center` tampil di bawah `Add-ons`

### Staff tidak melihat menu dan URL langsung menampilkan empty state
23. Masuk sebagai `Sari Staff {runId}`
24. Verifikasi menu `Dashboard` tampil pada sidebar
25. Verifikasi menu `Service Center` tidak tampil pada sidebar
26. Buka halaman daftar Service Center lewat alamat langsung
27. Verifikasi empty state `You do not have access to Service Center.` tampil
28. Verifikasi nama `Servis Rahasia {runId}` tidak tampil pada halaman

### Approver tidak melihat menu dan URL langsung menampilkan empty state
29. Masuk sebagai `Anton Approver {runId}`
30. Verifikasi menu `Dashboard` tampil pada sidebar
31. Verifikasi menu `Service Center` tidak tampil pada sidebar
32. Buka halaman daftar Service Center lewat alamat langsung
33. Verifikasi empty state `You do not have access to Service Center.` tampil
34. Verifikasi nama `Servis Rahasia {runId}` tidak tampil pada halaman

### Akses tanpa sesi login diarahkan ke halaman login
35. Buka halaman daftar Service Center lewat alamat langsung tanpa sesi login
36. Verifikasi pengguna diarahkan ke halaman login
