---
id: TC-FA-FASVC-BE-075-be-batas-jumlah-master-data
title: "Server: Master Data Count Limit: Submit Melampaui Batas Ditolak Tanpa Mutasi dan Tanpa Log"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["FASVC-LOGIC-12a", "EB-CON-4", "§9.2#r3"]
smoke: []
dependsOn: []
trace:
  "FASVC-LOGIC-12a": [2, 5, 9, 16, 18, 20, 22, 24, 26]
  "EB-CON-4": [5, 7, 16]
  "§9.2#r3": [2, 11, 16]
anchor: []
---

# Server: Master Data Count Limit: Submit Melampaui Batas Ditolak Tanpa Mutasi dan Tanpa Log

## Prerequisites
- Aktor: Total Control `Dewi Anggraini {runId}` dan Total Control `Budi Santoso {runId}` pada entitas khusus `Klien Batas Layanan {runId}`.
- Data:
  - DU-075-1: Entitas khusus `Klien Batas Layanan {runId}` berstatus `Active`, dengan lisensi addon Maintenance aktif, tidak dipakai spec lain.
  - DU-075-2: User `Dewi Anggraini {runId}` dengan Role `Total Control`, dan cakupan Group seluruh pohon Group pada `Klien Batas Layanan {runId}`.
  - DU-075-3: User `Budi Santoso {runId}` dengan Role `Total Control`, dan cakupan Group seluruh pohon Group pada `Klien Batas Layanan {runId}`.
  - DU-075-4: Service Center `Service Center Massal {n} {runId}`, 998 record (n = 1 sampai 998), Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, Company email `kontak@batas075.co.id`, Status `Active`, pada `Klien Batas Layanan {runId}`.
  - DU-075-5: Service Center `Service Center Massal Nonaktif {runId}`, Service type `Repair`, Available to `All groups`, Country `Indonesia`, City `Bandung`, Company email `kontak@batas075.co.id`, Status `Inactive`, pada `Klien Batas Layanan {runId}`.
- Kondisi:
  - Spec ini memakai entitas khusus DU-075-1 yang tidak dipakai spec lain; lisensi addon Maintenance aktif pada entitas itu.
  - Master Data Count Limit bernilai `1000`, nilai terendah dalam rentang yang dapat diatur.
  - Entitas khusus `Klien Batas Layanan {runId}` sudah berisi tepat 999 Service Center pada semua status, yaitu DU-075-4 dan DU-075-5.

## Test Steps
### Satu slot tersisa direbut dua aktor: satu Submit berhasil dan satu ditolak
1. Baca daftar Service Center `Klien Batas Layanan {runId}` sebagai Total Control dengan pencarian `Service Center Massal` dan catat jumlah barisnya sebagai N0
2. Verifikasi N0 adalah 999, terdiri dari 998 Active dan 1 Inactive, sehingga tersisa tepat satu slot sebelum Master Data Count Limit `1000`
3. Baca Changelog Service Center dengan Service Center Name `Mitra Perawatan Cepat {runId}` dan Name `Mitra Perawatan Lambat {runId}` dan catat jumlah entri Action `Created` sebagai L0
4. `Dewi Anggraini {runId}` mengirim Create dengan Name `Mitra Perawatan Cepat {runId}` dan `Budi Santoso {runId}` mengirim Create dengan Name `Mitra Perawatan Lambat {runId}` bersamaan, masing-masing dengan Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, dan Company email `kontak@batas075.co.id`
5. Verifikasi tepat satu dari kedua permintaan berhasil dan satu lagi ditolak dengan pesan `You've reached the platform limit of 1000 service centers. Contact support if you need a higher limit.`
6. Baca ulang daftar Service Center `Klien Batas Layanan {runId}` sebagai Total Control dengan pencarian `Mitra Perawatan`
7. Verifikasi hasil memuat tepat satu Service Center, yaitu yang permintaannya berhasil
8. Baca ulang Changelog Service Center dengan Service Center Name `Mitra Perawatan Cepat {runId}` dan Name `Mitra Perawatan Lambat {runId}`
9. Verifikasi jumlah entri Action `Created` bertambah tepat satu dari L0, sehingga permintaan yang ditolak tidak menulis log

### Submit pada batas tercapai ditolak tanpa mutasi dan tanpa log
10. Baca ulang daftar Service Center `Klien Batas Layanan {runId}` sebagai Total Control dengan pencarian `Service Center Massal` dan catat jumlah barisnya sebagai N1
11. Verifikasi N1 tetap 999
12. Baca Changelog Service Center dengan Service Center Name `Sentral Teknik Tambahan {runId}` dan catat jumlah entrinya sebagai L1
13. Baca Activity Log dengan Object `Service Center` dan Name `Sentral Teknik Tambahan {runId}` dan catat jumlah entrinya sebagai A1
14. Baca System Log Detail User `Dewi Anggraini {runId}` dan catat jumlah entri Action `Created` sebagai S1
15. `Dewi Anggraini {runId}` mengirim Create dengan Name `Sentral Teknik Tambahan {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Jakarta Selatan`, dan Company email `kontak@batas075.co.id`, padahal total Service Center di `Klien Batas Layanan {runId}` sudah mencapai `1000`
16. Verifikasi permintaan ditolak dengan pesan `You've reached the platform limit of 1000 service centers. Contact support if you need a higher limit.`
17. Baca daftar Service Center `Klien Batas Layanan {runId}` sebagai Total Control dengan pencarian `Sentral Teknik Tambahan {runId}`
18. Verifikasi hasil pencarian kosong, sehingga Create yang melampaui batas tidak membuat Service Center
19. Baca ulang Changelog Service Center dengan Service Center Name `Sentral Teknik Tambahan {runId}`
20. Verifikasi jumlah entri tetap L1
21. Baca ulang Activity Log dengan Object `Service Center` dan Name `Sentral Teknik Tambahan {runId}`
22. Verifikasi jumlah entri tetap A1
23. Baca ulang System Log Detail User `Dewi Anggraini {runId}`
24. Verifikasi jumlah entri Action `Created` tetap S1
25. Baca ulang daftar Service Center `Klien Batas Layanan {runId}` sebagai Total Control dengan pencarian `Service Center Massal` dan catat jumlah barisnya sebagai N2
26. Verifikasi N2 tetap 999, termasuk satu Service Center yang berstatus `Inactive`
