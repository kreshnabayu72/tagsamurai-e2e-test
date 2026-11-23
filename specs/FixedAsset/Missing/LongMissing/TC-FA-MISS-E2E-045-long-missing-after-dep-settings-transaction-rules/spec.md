---
id: TC-FA-MISS-E2E-045-long-missing-after-dep-settings-transaction-rules
title: "Long missing after: nilai setting menentukan penanda pada evaluasi berikutnya; 0 menonaktifkan"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.5#r5", "§11#r8", "§1.2#r114", "§1.2#r117", "§9.4.2#r19", "§9.4.1#r11", "§9.2#b55", "§9.2#b60"]
smoke: []
dependsOn: ["Settings Transaction Rules: Long missing after"]
trace:
  "§9.5#r5": [1]
  "§11#r8": [1, 39]
  "§1.2#r114": [5, 39]
  "§1.2#r117": [40]
  "§9.4.2#r19": [15]
  "§9.4.1#r11": [7, 15]
  "§9.2#b55": [15]
  "§9.2#b60": [23, 39]
anchor: [31]
coverage:
  web: automated
---

# Long missing after: nilai setting menentukan penanda pada evaluasi berikutnya; 0 menonaktifkan

## Prerequisites
- Aktor: Total Control `Rina W`.
- Layar awal: Settings Transaction Rules.
- Data:
  - DU-045-1: Asset `Laptop Lenovo ThinkPad T14 {runId}`, Group `Head Office`, dengan record Missing berstatus `Missing` yang dilaporkan pada `T0 − 34 hari`.
  - DU-045-2: Asset `Toyota Innova {runId}`, Group `Branch Surabaya`, dengan record Missing berstatus `Missing` yang dilaporkan pada `T0 − 10 hari`.
  - DU-045-3: Pengguna `Rina W`, Total Control.
- Kondisi:
  - Long missing after bernilai `30` sebelum spec ini mengubahnya.

## Test Steps

### Penanda Long missing pada nilai bawaan
1. Verifikasi nilai Long missing after `30` tampil pada Settings Transaction Rules
2. Buka halaman `Assets`
3. Klik tab `Missing`
4. Ketik Search `Laptop Lenovo ThinkPad T14 {runId}`, tekan Enter
5. Verifikasi kolom Days Missing pada baris `Laptop Lenovo ThinkPad T14 {runId}` memuat penanda `Long missing`
6. Ganti isi kotak search dengan `Toyota Innova {runId}`, tekan Enter
7. Verifikasi kolom Days Missing pada baris `Toyota Innova {runId}` tidak memuat penanda `Long missing`

### Nilai diturunkan menghitung ulang penanda pada evaluasi berikutnya
8. Buka Settings Transaction Rules
9. Ubah Long missing after menjadi `7`
10. Simpan perubahan Settings Transaction Rules
11. Job harian Long missing berjalan
12. Buka halaman `Assets`
13. Klik tab `Missing`
14. Ketik Search `Toyota Innova {runId}`, tekan Enter
15. Verifikasi kolom Days Missing pada baris `Toyota Innova {runId}` memuat penanda `Long missing`

### Nilai dinaikkan menghilangkan penanda
16. Buka Settings Transaction Rules
17. Ubah Long missing after menjadi `60`
18. Simpan perubahan Settings Transaction Rules
19. Job harian Long missing berjalan
20. Buka halaman `Assets`
21. Klik tab `Missing`
22. Ketik Search `Laptop Lenovo ThinkPad T14 {runId}`, tekan Enter
23. Verifikasi baris `Laptop Lenovo ThinkPad T14 {runId}` berstatus `Missing` dengan kolom Days Missing tanpa penanda `Long missing`

### Nilai 0 menghilangkan penanda yang sudah ada tanpa menutup record, lalu nilai dikembalikan
24. Buka Settings Transaction Rules
25. Ubah Long missing after menjadi `7`
26. Simpan perubahan Settings Transaction Rules
27. Job harian Long missing berjalan
28. Buka halaman `Assets`
29. Klik tab `Missing`
30. Ketik Search `Toyota Innova {runId}`, tekan Enter
31. Verifikasi kolom Days Missing pada baris `Toyota Innova {runId}` memuat penanda `Long missing` sebelum nilai diubah menjadi `0`
32. Buka Settings Transaction Rules
33. Ubah Long missing after menjadi `0`
34. Simpan perubahan Settings Transaction Rules
35. Job harian Long missing berjalan
36. Buka halaman `Assets`
37. Klik tab `Missing`
38. Ketik Search `Toyota Innova {runId}`, tekan Enter
39. Verifikasi baris `Toyota Innova {runId}` berstatus `Missing` dengan kolom Days Missing tanpa penanda `Long missing`
40. Verifikasi baris `Toyota Innova {runId}` tetap tampil di sub-tab Active
41. Buka Settings Transaction Rules
42. Ubah Long missing after menjadi `30`
43. Simpan perubahan Settings Transaction Rules
