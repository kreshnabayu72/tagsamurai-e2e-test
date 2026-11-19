---
id: TC-FA-FASVC-BE-072-be-isolasi-dan-cakupan-baca
title: "Server: Cakupan Baca per Client dan Group: Daftar, Detail, dan Changelog"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["FASVC-LOGIC-01b", "FASVC-LOGIC-01c", "FASVC-LOGIC-08a", "§2.2#r1", "§Aturan Logika Modul#p5", "§9.11#p2", "§10#b1"]
smoke: []
dependsOn: []
trace:
  "FASVC-LOGIC-01b": [2, 5]
  "FASVC-LOGIC-01c": [7, 13]
  "FASVC-LOGIC-08a": [7, 9, 11, 13]
  "§2.2#r1": [15, 21, 30, 32, 34, 36, 38, 40, 42, 44]
  "§Aturan Logika Modul#p5": [24, 26, 28]
  "§9.11#p2": [17, 19]
  "§10#b1": [3, 5]
anchor: []
---

# Server: Cakupan Baca per Client dan Group: Daftar, Detail, dan Changelog

## Prerequisites
- Aktor: Total Control pada client suite dan user pada Data sesuai langkah.
- Data:
  - DU-072-1: User `Rina Wulandari {runId}` dengan Role `Asset Admin`, Role Transaksi `Maintenance Routine`, dan cakupan Group `Cabang Surabaya {runId}` saja.
  - DU-072-2: User `Siti Rahmawati {runId}` dengan Role `Group Manager`, dan cakupan Group `Cabang Surabaya {runId}` saja.
  - DU-072-3: User `Eka Pratama {runId}` dengan Role `Monitoring & Report`, Role Transaksi `Maintenance Routine`, dan cakupan Group `Cabang Malang {runId}` saja.
  - DU-072-4: User `Yoga Saputra {runId}` dengan Role `Read Only`, dan cakupan Group `Cabang Bekasi {runId}` saja.
  - DU-072-5: User `Dewi Anggraini {runId}` dengan Role `Total Control`, dan cakupan Group seluruh pohon Group, pada client lain.
  - DU-072-6: Service Center `Servis Elektrik Surabaya {runId}`, Service type `Routine`, Available to `Cabang Surabaya {runId}`, Country `Indonesia`, City `Surabaya`, Company email `layanan@cakupanbaca.co.id`, Status `Active`, ada di client suite.
  - DU-072-7: Service Center `Servis Elektrik Malang {runId}`, Service type `Routine`, Available to `Cabang Malang {runId}`, Country `Indonesia`, City `Malang`, Company email `layanan@cakupanbaca.co.id`, Status `Active`, ada di client suite.
  - DU-072-8: Service Center `Servis Terpadu Jawa Timur {runId}`, Service type `Routine`, Available to `Cabang Surabaya {runId}` dan `Cabang Malang {runId}`, Country `Indonesia`, City `Surabaya`, Company email `layanan@cakupanbaca.co.id`, Status `Active`, ada di client suite.
  - DU-072-9: Service Center `PT Sejuk Abadi Teknik {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, Company email `layanan@cakupanbaca.co.id`, Status `Active`, ada di client suite.
  - DU-072-10: Service Center `Bengkel Bekasi Mandiri {runId}`, Service type `Routine`, Available to `Cabang Bekasi {runId}`, Country `Indonesia`, City `Bekasi`, Company email `layanan@cakupanbaca.co.id`, Status `Active`, ada di client suite.
  - DU-072-11: Service Center `Sinar Mitra Teknik {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Surabaya`, Company email `layanan@cakupanbaca.co.id`, Status `Active`, ada di client lain dan tidak ada di client suite.
  - Group `Cabang Surabaya {runId}`, `Cabang Malang {runId}`, dan `Cabang Bekasi {runId}` adalah anak langsung root pohon Group di client suite.
- Kondisi:
  - Lisensi addon Maintenance aktif pada client suite dan pada client lain.
  - Service Center `Servis Telah Dihapus {runId}` sudah dihapus dari client suite, sehingga ID-nya tidak ada.

## Test Steps
### Daftar hanya memuat Service Center milik client dan yang beririsan dengan cakupan Group
1. Baca daftar Service Center client suite sebagai Total Control dengan pencarian `{runId}`
2. Verifikasi hasil memuat tepat `Servis Elektrik Surabaya {runId}`, `Servis Elektrik Malang {runId}`, `Servis Terpadu Jawa Timur {runId}`, `PT Sejuk Abadi Teknik {runId}`, dan `Bengkel Bekasi Mandiri {runId}` dalam satu daftar, tanpa memandang Available to-nya
3. Verifikasi hasil tidak memuat `Sinar Mitra Teknik {runId}` yang milik client lain
4. Baca daftar Service Center sebagai `Dewi Anggraini {runId}`, Total Control client lain, dengan pencarian `{runId}`
5. Verifikasi hasil memuat tepat `Sinar Mitra Teknik {runId}`
6. Baca daftar Service Center sebagai `Rina Wulandari {runId}` dengan pencarian `{runId}`
7. Verifikasi hasil memuat tepat `Servis Elektrik Surabaya {runId}`, `Servis Terpadu Jawa Timur {runId}`, dan `PT Sejuk Abadi Teknik {runId}`, karena Available to-nya beririsan dengan cakupan Asset Admin dan `All groups` terlihat semua
8. Baca daftar Service Center sebagai `Siti Rahmawati {runId}` dengan pencarian `{runId}`
9. Verifikasi hasil memuat tepat `Servis Elektrik Surabaya {runId}`, `Servis Terpadu Jawa Timur {runId}`, dan `PT Sejuk Abadi Teknik {runId}` untuk Group Manager
10. Baca daftar Service Center sebagai `Eka Pratama {runId}` dengan pencarian `{runId}`
11. Verifikasi hasil memuat tepat `Servis Elektrik Malang {runId}`, `Servis Terpadu Jawa Timur {runId}`, dan `PT Sejuk Abadi Teknik {runId}` untuk Monitoring & Report
12. Baca daftar Service Center sebagai `Yoga Saputra {runId}` dengan pencarian `{runId}`
13. Verifikasi hasil memuat tepat `PT Sejuk Abadi Teknik {runId}` dan `Bengkel Bekasi Mandiri {runId}` untuk Read Only, termasuk `All groups` yang terlihat semua

### Detail dan Changelog gabungan mengikuti cakupan baca
14. Baca Detail Service Center `Servis Elektrik Surabaya {runId}` sebagai `Rina Wulandari {runId}`
15. Verifikasi Detail terbuka dan memuat Name `Servis Elektrik Surabaya {runId}`
16. Baca Detail Service Center `Servis Terpadu Jawa Timur {runId}` sebagai `Rina Wulandari {runId}`
17. Verifikasi Detail terbuka dan memuat Name `Servis Terpadu Jawa Timur {runId}`, walau Available to-nya sebagian di luar cakupan, karena cakupan baca adalah beririsan
18. `Rina Wulandari {runId}` mengirim Inactivate atas `Servis Terpadu Jawa Timur {runId}` yang baru terbaca
19. Verifikasi Inactivate atas `Servis Terpadu Jawa Timur {runId}` ditolak dengan pesan `You don't have permission to do this.`, karena cakupan tulis harus seluruhnya dalam cakupan sedangkan cakupan baca cukup beririsan
20. Baca Changelog Service Center sebagai `Rina Wulandari {runId}` dengan pencarian `{runId}`
21. Verifikasi entri Changelog hanya berasal dari Service Center `Servis Elektrik Surabaya {runId}`, `Servis Terpadu Jawa Timur {runId}`, dan `PT Sejuk Abadi Teknik {runId}`

### Detail di luar cakupan dan ID yang tidak ada dijawab sama, sedangkan permintaan tulis dibedakan
22. Baca Detail Service Center `Servis Telah Dihapus {runId}` yang ID-nya tidak ada sebagai `Rina Wulandari {runId}` dan catat responsnya sebagai R1
23. Baca Detail Service Center `Servis Elektrik Malang {runId}` yang Available to-nya tidak beririsan dengan cakupan `Rina Wulandari {runId}` dan catat responsnya sebagai R2
24. Verifikasi R2 sama dengan R1, yaitu tidak ditemukan, sehingga keberadaan Service Center di luar cakupan tidak terungkap
25. `Siti Rahmawati {runId}` mengirim Inactivate atas `Bengkel Bekasi Mandiri {runId}` yang ada tetapi Available to-nya di luar cakupannya
26. Verifikasi Inactivate atas `Bengkel Bekasi Mandiri {runId}` ditolak karena pengirim tidak punya hak, dengan pesan `You don't have permission to do this.`
27. `Siti Rahmawati {runId}` mengirim Inactivate atas `Servis Telah Dihapus {runId}` yang ID-nya tidak ada
28. Verifikasi Inactivate atas ID yang tidak ada ditolak dengan pesan `This service center is no longer available.`

### Detail dan Changelog gabungan mengikuti cakupan baca untuk Group Manager, Monitoring & Report, Read Only, dan Total Control
29. Baca Detail Service Center `Servis Elektrik Surabaya {runId}` sebagai `Siti Rahmawati {runId}`
30. Verifikasi Detail terbuka dan memuat Name `Servis Elektrik Surabaya {runId}` untuk Group Manager
31. Baca Changelog Service Center sebagai `Siti Rahmawati {runId}` dengan pencarian `{runId}`
32. Verifikasi entri Changelog hanya berasal dari Service Center `Servis Elektrik Surabaya {runId}`, `Servis Terpadu Jawa Timur {runId}`, dan `PT Sejuk Abadi Teknik {runId}` untuk Group Manager
33. Baca Detail Service Center `Servis Elektrik Malang {runId}` sebagai `Eka Pratama {runId}`
34. Verifikasi Detail terbuka dan memuat Name `Servis Elektrik Malang {runId}` untuk Monitoring & Report
35. Baca Changelog Service Center sebagai `Eka Pratama {runId}` dengan pencarian `{runId}`
36. Verifikasi entri Changelog hanya berasal dari Service Center `Servis Elektrik Malang {runId}`, `Servis Terpadu Jawa Timur {runId}`, dan `PT Sejuk Abadi Teknik {runId}` untuk Monitoring & Report
37. Baca Detail Service Center `Bengkel Bekasi Mandiri {runId}` sebagai `Yoga Saputra {runId}`
38. Verifikasi Detail terbuka dan memuat Name `Bengkel Bekasi Mandiri {runId}` untuk Read Only
39. Baca Changelog Service Center sebagai `Yoga Saputra {runId}` dengan pencarian `{runId}`
40. Verifikasi entri Changelog hanya berasal dari Service Center `Bengkel Bekasi Mandiri {runId}` dan `PT Sejuk Abadi Teknik {runId}`, termasuk `All groups` yang terlihat semua untuk Read Only
41. Baca Detail Service Center `Servis Elektrik Malang {runId}` sebagai Total Control client suite
42. Verifikasi Detail terbuka dan memuat Name `Servis Elektrik Malang {runId}` untuk Total Control
43. Baca Changelog Service Center sebagai Total Control client suite dengan pencarian `{runId}`
44. Verifikasi entri Changelog hanya berasal dari Service Center `Servis Elektrik Surabaya {runId}`, `Servis Elektrik Malang {runId}`, `Servis Terpadu Jawa Timur {runId}`, `PT Sejuk Abadi Teknik {runId}`, dan `Bengkel Bekasi Mandiri {runId}`, tanpa `Sinar Mitra Teknik {runId}` yang milik client lain
