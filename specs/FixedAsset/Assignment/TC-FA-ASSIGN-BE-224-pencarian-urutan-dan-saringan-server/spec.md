---
id: TC-FA-ASSIGN-BE-224-pencarian-urutan-dan-saringan-server
title: "Hasil Search, Sort, dan Filter di server per kelas kolom"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-SRC-1", "EB-SRT-1", "EB-SRT-2", "EB-FLT-3"]
smoke: []
dependsOn: []
owner: BE
trace:
  "EB-SRC-1": [2, 4, 6, 8, 10, 12, 14, 16]
  "EB-SRT-1": [19, 21, 23, 25, 27]
  "EB-SRT-2": [28, 30, 32, 50, 52]
  "EB-FLT-3": [35, 38, 41, 44, 47]
---

# Hasil Search, Sort, dan Filter di server per kelas kolom

## Prerequisites
- Aktor: Aktor Assignment `Rina Wijaya {runId}` dan `Agus Pratama {runId}` (Asset Admin, cakupan Group `Head Office {runId}` dan `Branch Surabaya {runId}`); Assignee Employee dan PIC ber-akun login seperti di entri data.
- Data:
  - DU-224-1: User, Aktor Assignment dengan cakupan dua Group: Nama `Rina Wijaya {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId} dan Branch Surabaya {runId}`.
  - DU-224-2: User, Aktor Assignment kedua dengan cakupan dua Group: Nama `Agus Pratama {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId} dan Branch Surabaya {runId}`.
  - DU-224-3: Assignment, ASG pertama dibuat: Employee, Head Office, Waiting for Handover, Total Asset 1: Assignee `anggur Wijaya {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kursi Kerja Alfa {runId}`, Status `Waiting for Handover`, Total Asset `1`, Requested By `Rina Wijaya {runId}`.
  - DU-224-4: Assignment, ASG kedua dibuat: Employee, Head Office, Waiting for Handover, Total Asset 2: Assignee `Apel Susanto {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Meja Kerja Beta {runId}`, Baris 2 `Lemari Kerja Beta {runId}`, Status `Waiting for Handover`, Total Asset `2`, Requested By `Agus Pratama {runId}`.
  - DU-224-5: Assignment, ASG ketiga dibuat: Employee, Head Office, Waiting for Approval, Total Asset 10: Assignee `Bravo Hidayat {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris `Rak Arsip Gamma {n} {runId}`, Status `Waiting for Approval`, Total Asset `10`, Requested By `Rina Wijaya {runId}`.
  - DU-224-6: Assignment, ASG keempat dibuat: Division, Branch Surabaya, Assigned, Total Asset 1: Assignee `Delta Logistik {runId}`, Tipe Assignee `Division`, Group `Branch Surabaya {runId}`, Baris 1 `Genset Delta {runId}`, Status `Assigned`, Total Asset `1`, Requested By `Agus Pratama {runId}`, PIC `Wati Susanti {runId}`.
  - DU-224-7: Assignment, ASG kelima dibuat: Employee, Branch Surabaya, Assigned, Total Asset 2: Assignee `Echo Wibowo {runId}`, Tipe Assignee `Employee`, Group `Branch Surabaya {runId}`, Baris 1 `Motor Echo A {runId}`, Baris 2 `Motor Echo B {runId}`, Status `Assigned`, Total Asset `2`, Requested By `Rina Wijaya {runId}`.
  - DU-224-9: Assignment, ASG dengan tiga baris Assigned yang salah satunya tanpa Brand: Assignee `Foxtrot Maulana {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Router TP-Link Foxtrot {runId}`, Baris 2 `Switch Foxtrot {runId}`, Baris 3 `Kabel Roll Foxtrot {runId}`, Status baris `Assigned`, Brand baris 1 `TP-Link`, Brand baris 2 `Cisco`, Brand baris 3 `—`.
- Kondisi:
  - Kelima ASG di atas dibuat berurutan menurut urutan DU-224-3 sampai DU-224-7, sehingga Request Date DU-224-3 lebih lama daripada DU-224-4 dan seterusnya.
  - Semua pengamatan memakai Search `{runId}` pada tab Transactions sehingga hanya ASG spec ini yang diamati.

## Test Steps

### Search mencocokkan substring dan tidak peka huruf besar kecil
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi tepat lima ASG milik spec ini tampil sebagai pembanding hasil Search
3. Ketik Search `ANGGUR wijaya {runId}`, tekan Enter
4. Verifikasi hanya ASG `anggur Wijaya {runId}` yang tampil karena substring dan huruf besar kecil sama-sama cocok pada kolom Assignee
5. Ketik Search `division {runId}`, tekan Enter
6. Verifikasi hanya ASG `Delta Logistik {runId}` yang tampil karena kata kunci cocok pada kolom Assignee Type bertipe badge
7. Ketik Search `waiting for handover {runId}`, tekan Enter
8. Verifikasi ASG `anggur Wijaya {runId}` dan `Apel Susanto {runId}` tampil karena kata kunci cocok pada kolom Status bertipe badge
9. Ketik Search `Branch Surabaya {runId}`, tekan Enter
10. Verifikasi ASG `Delta Logistik {runId}` dan `Echo Wibowo {runId}` tampil karena kata kunci cocok pada kolom Group bertipe badge
11. Ketik Search `Agus Pratama {runId}`, tekan Enter
12. Verifikasi ASG `Apel Susanto {runId}` dan `Delta Logistik {runId}` tampil karena kata kunci cocok pada kolom Requested By
13. Ketik Search `Kursi Kerja Alfa {runId}`, tekan Enter
14. Verifikasi ASG `anggur Wijaya {runId}` tampil karena kata kunci cocok pada nama aset di dalam ASG
15. Ketik Search `zzz tanpa kecocokan {runId}`, tekan Enter
16. Verifikasi hasil Search kosong dan tabel menampilkan `No results found`

### Sort teks, angka, badge, dan tanggal
17. Ketik Search `{runId}`, tekan Enter
18. Rina mengurutkan kolom Assignee Ascending
19. Verifikasi urutan Assignee Ascending adalah `anggur Wijaya {runId}`, `Apel Susanto {runId}`, `Bravo Hidayat {runId}`, `Delta Logistik {runId}`, `Echo Wibowo {runId}` karena teks diurutkan tanpa peka huruf besar kecil
20. Rina mengurutkan kolom Assignee Descending
21. Verifikasi urutan Assignee Descending adalah kebalikan penuh dari urutan Ascending
22. Rina mengurutkan kolom Total Asset Ascending
23. Verifikasi urutan Total Asset Ascending adalah ASG bernilai `1`, `1`, `2`, `2`, `10` secara natural dan bukan `1`, `1`, `10`, `2`, `2`
24. Rina mengurutkan kolom Status Ascending
25. Verifikasi urutan Status Ascending mengikuti label badge secara alfabet: `Assigned`, lalu `Waiting for Approval`, lalu `Waiting for Handover`
26. Rina mengurutkan kolom Request Date Oldest First
27. Verifikasi urutan Request Date Oldest First sama dengan urutan pembuatan DU-224-3 sampai DU-224-7 dan Newest First adalah kebalikannya

### Nilai kosong dan nilai sama diurutkan menurut default sort
28. Verifikasi kolom Assignee, Total Asset, Status, dan Request Date tidak pernah kosong pada kelima ASG sehingga tidak ada posisi nilai kosong yang perlu ditetapkan
29. Rina mengurutkan kolom Total Asset Ascending dan memeriksa dua ASG bernilai `1` serta dua ASG bernilai `2`
30. Verifikasi ASG bernilai sama diurutkan menurut default sort tabel: `anggur Wijaya {runId}` yang `Waiting for Handover` lebih dulu daripada `Delta Logistik {runId}` yang `Assigned`, dan `Apel Susanto {runId}` lebih dulu daripada `Echo Wibowo {runId}`
31. Rina mengurutkan kolom Total Asset Descending
32. Verifikasi urutan antar baris bernilai sama tidak berubah antar permintaan dan antar halaman, tanpa baris ganda atau terlewat

### Filter AND antar field dan OR dalam satu field
33. Rina memilih filter Status `Waiting for Handover` dan `Assigned` dengan Search `{runId}` aktif
34. Klik `[Apply]`
35. Verifikasi ASG `anggur Wijaya {runId}`, `Apel Susanto {runId}`, `Delta Logistik {runId}`, dan `Echo Wibowo {runId}` tampil karena dua opsi dalam satu field berlaku OR
36. Rina menambahkan filter Group `Head Office {runId}`
37. Klik `[Apply]`
38. Verifikasi hanya ASG `anggur Wijaya {runId}` dan `Apel Susanto {runId}` tampil karena dua field berbeda berlaku AND
39. Rina menambahkan filter Requested By `Agus Pratama {runId}`
40. Klik `[Apply]`
41. Verifikasi hanya ASG `Apel Susanto {runId}` tampil karena ketiga field berlaku AND
42. Rina mengganti filter Assignee Type menjadi `Division` dan `Employee` dengan filter Status dan Group dikosongkan
43. Klik `[Apply]`
44. Verifikasi kelima ASG tampil karena `Division` OR `Employee` dalam satu field mencakup semuanya
45. Rina mengosongkan filter dan mengisi filter Total Asset Min `2` dan Max `10`
46. Klik `[Apply]`
47. Verifikasi ASG `Apel Susanto {runId}`, `Bravo Hidayat {runId}`, dan `Echo Wibowo {runId}` tampil karena batas Min dan Max inklusif

### Nilai kosong diurutkan di akhir pada kedua arah
48. Ketik Search `Foxtrot Maulana {runId}` pada tab Assigned Assets By Asset, tekan Enter
49. Rina mengurutkan kolom Brand Ascending
50. Verifikasi urutan Brand Ascending adalah `Cisco`, `TP-Link`, lalu baris `Kabel Roll Foxtrot {runId}` yang Brand-nya `—` di akhir
51. Rina mengurutkan kolom Brand Descending
52. Verifikasi urutan Brand Descending adalah `TP-Link`, lalu `Cisco`, lalu baris `Kabel Roll Foxtrot {runId}` yang Brand-nya `—` tetap di akhir[^drift-1]

[^drift-1]: Drift foundation vs kontrak komponen. PRD: tidak menetapkan posisi nilai kosong pada sort. foundation `prd-conventions.md` §9.15: nilai kosong di akhir saat ascending dan di awal saat descending. Kontrak `DataTable#6`: an empty (null/undefined) value goes last in both directions. Diasersi: kontrak, karena foundation meminta mekanik yang tidak bisa terjadi bersama butir `Does` komponen (SB-7).
