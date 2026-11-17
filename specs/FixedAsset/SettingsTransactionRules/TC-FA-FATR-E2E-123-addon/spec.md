---
id: TC-FA-FATR-E2E-123-addon
title: "Addon Audit dan Maintenance: tab dan baris Geolocation menurut status addon"
layer: ui-e2e
priority: High
caseType: Negative
status: ready-for-automation
sourceRules: ["§9.4.2#r66", "§9.4.2#r69", "§9.4.2#r72", "§9.10.5#b1", "§9.10.5#b2", "§9.10.5#b6", "§11#r20", "§4.3#r24", "§Aturan Logika Modul#r113", "§9.4.2#r67", "§9.10.5#b5", "§4.3#r21", "§4.3#r22", "§4.3#r23"]
smoke: ["§4.3#r21", "§4.3#r22", "§4.3#r23"]
dependsOn: []
trace:
  "§9.4.2#r66": [21, 45]
  "§9.4.2#r69": [14, 18, 41]
  "§9.4.2#r72": [25, 29, 32, 43]
  "§9.10.5#b1": [14, 21, 41, 45]
  "§9.10.5#b2": [25, 32, 43, 46]
  "§9.10.5#b6": 48
  "§11#r20": [21, 32, 36]
  "§4.3#r24": [36, 45, 46]
  "§Aturan Logika Modul#r113": 36
  "§9.4.2#r67": [36, 45, 46]
  "§9.10.5#b5": [36, 45, 46]
  "§4.3#r21": [21, 32, 45, 46]
  "§4.3#r22": [14, 16, 18]
  "§4.3#r23": [25, 27, 29]
anchor: [6, 8, 10, 11, 20, 31, 35]
coverage:
  web: automated
---

# Addon Audit dan Maintenance: tab dan baris Geolocation menurut status addon

## Prerequisites
- Aktor: Total Control. Operator Admin Console memicu perubahan alokasi lisensi addon entitas.
- Layar awal: Fixed Asset > Settings > Transaction Settings.
- Data:
  - DU-123-1: Entitas `Citra Addon {runId}`, entitas khusus yang tidak dipakai spec lain. Subscription FAMS-nya memiliki alokasi lisensi addon Audit dan Maintenance, sehingga kedua addon aktif.
- Kondisi:
  - Nilai tersimpan di Company default entitas DU-123-1: Grace period `5`, Reminder before due `7`, Require location Audit `ON`, Require location Maintenance `ON`.

## Test Steps

### Kedua addon aktif: tab Audit, Maintenance, dan Geolocation dapat dipakai
1. Klik `All categories` pada Sidebar Category Tree
2. Klik ikon Changelog di header
3. Catat jumlah baris tabel Changelog
4. Tekan `Esc` untuk menutup dialog Changelog
5. Klik tab `Audit`
6. Verifikasi field `Grace period` bernilai `5`
7. Klik tab `Maintenance`
8. Verifikasi field `Reminder before due` bernilai `7`
9. Klik tab `Geolocation`
10. Verifikasi baris `Audit` pada Require location tampil
11. Verifikasi baris `Maintenance` pada Require location tampil

### Addon Audit tidak aktif dan Maintenance aktif: tab Audit disabled dan baris Audit tidak tampil
12. Operator mencabut alokasi lisensi addon bagi tab `Audit` dari subscription FAMS entitas `Citra Addon {runId}`
13. Muat ulang halaman
14. Verifikasi tab `Audit` disabled
15. Arahkan pointer ke tab `Audit`
16. Verifikasi alasan `Requires the Audit add-on.` tersampaikan pada tab `Audit` yang disabled
17. Klik tab `Audit`
18. Verifikasi tab `Audit` tidak menjadi tab aktif
19. Klik tab `Geolocation`
20. Verifikasi baris `Maintenance` pada Require location tampil
21. Verifikasi baris `Audit` pada Require location tidak tampil

### Addon Maintenance tidak aktif dan Audit aktif: tab Maintenance disabled dan baris Maintenance tidak tampil
22. Operator mengalokasikan kembali lisensi addon bagi tab `Audit` ke subscription FAMS entitas `Citra Addon {runId}`
23. Operator mencabut alokasi lisensi addon bagi tab `Maintenance` dari subscription FAMS entitas `Citra Addon {runId}`
24. Muat ulang halaman
25. Verifikasi tab `Maintenance` disabled
26. Arahkan pointer ke tab `Maintenance`
27. Verifikasi alasan `Requires the Maintenance add-on.` tersampaikan pada tab `Maintenance` yang disabled
28. Klik tab `Maintenance`
29. Verifikasi tab `Maintenance` tidak menjadi tab aktif
30. Klik tab `Geolocation`
31. Verifikasi baris `Audit` pada Require location tampil
32. Verifikasi baris `Maintenance` pada Require location tidak tampil

### Kedua addon tidak aktif: tab Geolocation tidak tampil
33. Operator mencabut alokasi lisensi addon bagi tab `Audit` dari subscription FAMS entitas `Citra Addon {runId}`
34. Muat ulang halaman
35. Verifikasi tab `Audit` disabled
36. Verifikasi tab `Geolocation` tidak tampil di daftar tab

### Nilai tersimpan dipertahankan saat addon aktif kembali
37. Operator mengalokasikan kembali lisensi addon bagi tab `Audit` ke subscription FAMS entitas `Citra Addon {runId}`
38. Operator mengalokasikan kembali lisensi addon bagi tab `Maintenance` ke subscription FAMS entitas `Citra Addon {runId}`
39. Muat ulang halaman
40. Klik tab `Audit`
41. Verifikasi field `Grace period` bernilai `5`
42. Klik tab `Maintenance`
43. Verifikasi field `Reminder before due` bernilai `7`
44. Klik tab `Geolocation`
45. Verifikasi baris `Audit` pada Require location tetap bernilai `ON` seperti sebelum addon dicabut
46. Verifikasi baris `Maintenance` pada Require location tetap bernilai `ON` seperti sebelum addon dicabut

### Perubahan status addon tidak menambah entri Changelog
47. Klik ikon Changelog di header
48. Verifikasi jumlah baris tabel Changelog sama dengan jumlah yang dicatat sebelum perubahan status addon
49. Tekan `Esc` untuk menutup dialog Changelog
