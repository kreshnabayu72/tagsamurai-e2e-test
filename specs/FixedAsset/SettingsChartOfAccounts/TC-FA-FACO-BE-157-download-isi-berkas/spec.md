---
id: TC-FA-FACO-BE-157-download-isi-berkas
title: "Isi berkas Download Account List"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
owner: BE
sourceRules: ["§5#b7", "§[F-FACO-11] Download Account List#p1", "§[F-FACO-11] Download Account List#r2", "§9.4.2#r27", EB-DL-4, EB-DL-5]
smoke: []
dependsOn: []
trace:
  "§5#b7": [2, 3, 4, 8, 9, 11, 13, 16]
  "§[F-FACO-11] Download Account List#p1": [2, 11, 22, 24]
  "§[F-FACO-11] Download Account List#r2": [22]
  "§9.4.2#r27": [22]
  EB-DL-4: [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 16, 18, 20]
  EB-DL-5: [22]
---

# Isi berkas Download Account List

## Prerequisites
- Aktor: Admin A (DU-157-1), Total Control dengan cakupan seluruh client.
- Data:
  - DU-157-1: User `Maya Pengelola {runId}`, Access Level `Total Control`, cakupan seluruh client.
  - DU-157-2: User `Siti Nur Rahmawati {runId}`, Access Level `Total Control`, cakupan seluruh client, nama dengan last name dua kata.
  - DU-157-3: Account Code `DLA-{runId}`, Account Name `Kas Satu Unduh {runId}`, Account Function `Asset Cost`, Status `Active`, Last Used in Journal `Oct 2026`, Used By 0.
  - DU-157-4: Account Code `DLB-{runId}`, Account Name `Akumulasi Dua Unduh {runId}`, Account Function `Accumulated Depreciation`, Status `Inactive`, Last Used in Journal kosong, Used By 0.
  - DU-157-5: Account Code `DLC-{runId}`, Account Name `Beban Sewa, Gedung Unduh {runId}`, Account Function `Depreciation Expense`, Status `Active`, Used By 0.
  - DU-157-6: Account Code `DLD-{runId}`, Account Name `Laba "Lain" Pelepasan Unduh {runId}`, Account Function `Gain on Disposal`, Status `Active`, Used By 0.
  - DU-157-7: Account Code `DLE-{runId}`, Account Name `Café Élan Unduh {runId}`, Account Function `Loss on Disposal`, Status `Active`, Used By 0.
  - DU-157-8: Account Code `DLF-{runId}`, Account Name `Lawan Kapitalisasi Unduh {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By 0.
  - DU-157-10: Account Code `DLG-{runId}`, Account Name `Hasil Pelepasan Unduh {runId}`, Account Function `Disposal Proceeds`, Status `Inactive`, Used By 0.
  - DU-157-12: 5001 akun volume dengan Account Code `W{n}-{runId}` dan Account Name `Volume Besar {runId} nomor {n}` (n dari 1 sampai 5001), Account Function `Asset Cost`, Status `Active`.
- Kondisi:
  - Akun `DLA-{runId}` sudah pernah diekspor pada periode `Oct 2026`; akun lain belum pernah diekspor.
  - Batas jumlah akun client mencukupi untuk 5001 akun volume tambahan.
  - Date Format `dd/MM/yy` dan Time Format `24h`.

## Test Steps

### Berkas CSV memuat nilai sel sesuai format PRD
1. Admin A mengirim Download as CSV dengan Search `Unduh {runId}`, dengan kolom visible Active, Account Code, Account Name, Function, Used By, Last Used in Journal, dan Modified By, dan tanpa Sort selain urutan default
2. Verifikasi berkas bernama `Chart-of-Accounts` berekstensi `.csv`, berpemisah koma, berenkoding UTF-8 dengan BOM, baris pertamanya berisi header Active, Account Code, Account Name, Function, Used By, Last Used in Journal, dan Modified By, dan berisi tepat tujuh baris data, satu per akun `DLA-{runId}` sampai `DLG-{runId}`, tanpa kolom foto dan tanpa kolom aksi
3. Verifikasi kolom Active berisi `Active` untuk akun `DLA-{runId}` dan `Inactive` untuk akun `DLB-{runId}`
4. Verifikasi kolom Function berisi label teks apa adanya: `Asset Cost` untuk `DLA-{runId}`, `Accumulated Depreciation` untuk `DLB-{runId}`, `Depreciation Expense` untuk `DLC-{runId}`, `Gain on Disposal` untuk `DLD-{runId}`, `Loss on Disposal` untuk `DLE-{runId}`, `Capitalization Offset` untuk `DLF-{runId}`, dan `Disposal Proceeds` untuk `DLG-{runId}`
5. Verifikasi sel Account Name akun `DLC-{runId}` yang mengandung koma dibungkus tanda kutip ganda sehingga isi sel `Beban Sewa, Gedung Unduh {runId}` tetap satu sel
6. Verifikasi sel Account Name akun `DLD-{runId}` yang mengandung tanda kutip dibungkus tanda kutip ganda dengan setiap kutip di dalam nilai digandakan menjadi dua tanda kutip berurutan, sehingga isi sel `Laba "Lain" Pelepasan Unduh {runId}` dapat dibaca kembali persis sama oleh pembaca CSV
7. Verifikasi sel Account Name akun `DLE-{runId}` terbaca utuh sebagai `Café Élan Unduh {runId}` dengan karakter beraksen tidak rusak
8. Verifikasi kolom Used By berisi angka `0` polos untuk ketujuh akun
9. Verifikasi kolom Last Used in Journal berisi periode `Oct 2026` untuk akun `DLA-{runId}`, dan berisi `-` (satu tanda hubung) untuk akun `DLB-{runId}` yang belum pernah diekspor, bukan sel kosong, bukan `—`, dan bukan `null`

### Berkas XLSX memuat nilai yang sama dalam satu sheet
10. Admin A mengirim Download as XLSX dengan Search `Unduh {runId}` dan kolom visible yang sama dengan unduhan CSV
11. Verifikasi berkas bernama `Chart-of-Accounts` berekstensi `.xlsx` dan memuat satu sheet bernama `Sheet1` dengan header serta tujuh baris data akun `DLA-{runId}` sampai `DLG-{runId}`
12. Verifikasi sel Used By ditulis sebagai sel angka `0`, bukan teks, dan kolom Active berisi `Active` atau `Inactive`
13. Verifikasi sel Last Used in Journal akun `DLA-{runId}` berisi `Oct 2026` dan akun `DLB-{runId}` berisi `-`

### Modified By ditulis dengan nama lengkap
14. Siti Nur Rahmawati (DU-157-2) mengirim Edit akun `DLF-{runId}` dengan Account Name `Lawan Kapitalisasi Revisi Unduh {runId}`
15. Admin A mengirim Download as CSV dengan Search `Unduh {runId}` dan kolom visible Active, Account Code, Account Name, Function, Used By, Last Used in Journal, dan Modified By
16. Verifikasi kolom Modified By pada baris akun `DLF-{runId}` berisi nama lengkap utuh `Siti Nur Rahmawati {runId}`, bukan format tampilan `Siti N`, dan kolom Account Name baris itu berisi `Lawan Kapitalisasi Revisi Unduh {runId}`

### Urutan baris berkas mengikuti Sort aktif
17. Admin A mengirim Download as CSV dengan Search `Unduh {runId}` dan Sort Account Code menurun
18. Verifikasi baris data berkas berurutan `DLG-{runId}`, `DLF-{runId}`, `DLE-{runId}`, `DLD-{runId}`, `DLC-{runId}`, `DLB-{runId}`, `DLA-{runId}`

### Hasil nol baris tetap menghasilkan berkas berisi header
19. Admin A mengirim Download as CSV dengan Search `Tidak Ada Unduh {runId}` yang tidak cocok dengan akun mana pun
20. Verifikasi permintaan berhasil dan berkas berisi hanya baris header kolom yang visible, tanpa baris data

### Berkas lengkap untuk lebih dari 5000 baris
21. Admin A mengirim Download as CSV dengan Search `Besar {runId}`, yang cocok dengan 5001 akun volume
22. Verifikasi berkas diterima langsung sebagai hasil permintaan itu, tanpa job latar belakang, dan berisi satu baris header serta tepat 5001 baris data, satu per akun volume, tanpa baris terpotong pada 5000

### Last Updated mengikuti Date Format dan Time Format client
23. Admin A mengirim Download as CSV dengan Search `Unduh {runId}` dan kolom visible Account Code dan Last Updated
24. Verifikasi sel Last Updated setiap baris data berisi tanggal berformat Date Format `dd/MM/yy` diikuti waktu berformat Time Format `24h` yang berlaku di client
