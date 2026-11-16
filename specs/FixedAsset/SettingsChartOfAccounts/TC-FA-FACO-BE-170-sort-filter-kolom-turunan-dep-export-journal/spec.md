---
id: TC-FA-FACO-BE-170-sort-filter-kolom-turunan-dep-export-journal
title: "Sort dan Filter atas kolom Used By dan Last Used in Journal"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: [EB-SRT-2, "§4.1.1#r5", "§4.1.1#r6", "§5#b5", "§9.5#r1"]
smoke: []
dependsOn: ["Export Journal: export jurnal yang mengisi Last Used in Journal", "Asset Class: pemakaian akun pada field akun Asset Class (Used By)"]
trace:
  EB-SRT-2: [10, 12, 14, 16]
  "§4.1.1#r5": [4, 6, 10, 12]
  "§4.1.1#r6": [2, 8, 14, 16]
  "§5#b5": [14, 16]
  "§9.5#r1": [14, 16]
---

# Sort dan Filter atas kolom Used By dan Last Used in Journal

## Prerequisites
- Aktor: Admin A (DU-170-1), Total Control dengan cakupan seluruh client.
- Data:
  - DU-170-1: User `Maya Pengelola {runId}`, Access Level `Total Control`, cakupan seluruh client.
  - DU-170-2: Account Code `SDA-{runId}`, Account Name `Kas Kecil Turunan {runId}`, Account Function `Asset Cost`, Status `Active`, Used By 0, Last Used in Journal kosong.
  - DU-170-3: Account Code `SDB-{runId}`, Account Name `Beban Mesin Turunan {runId}`, Account Function `Depreciation Expense`, Status `Active`, Used By 2, Last Used in Journal `Sep 2025`.
  - DU-170-4: Account Code `SDC-{runId}`, Account Name `Akumulasi Sewa Turunan {runId}`, Account Function `Accumulated Depreciation`, Status `Inactive`, Used By 0, Last Used in Journal `Jan 2026`.
  - DU-170-5: Account Code `SDD-{runId}`, Account Name `Kas Besar Turunan {runId}`, Account Function `Asset Cost`, Status `Active`, Used By 10, Last Used in Journal `Mar 2026`.
  - DU-170-6: Account Code `SDE-{runId}`, Account Name `Laba Pelepasan Turunan {runId}`, Account Function `Gain on Disposal`, Status `Inactive`, Used By 0, Last Used in Journal kosong.
  - DU-170-7: Account Code `SDF-{runId}`, Account Name `Kas Bank Turunan {runId}`, Account Function `Asset Cost`, Status `Active`, Used By 1, Last Used in Journal kosong.
- Kondisi:
  - Akun dengan Used By lebih dari 0 dipakai oleh Asset Class sebanyak nilai Used By-nya; akun dengan Last Used in Journal terisi sudah pernah diekspor pada periode itu.
  - Pada permintaan daftar, `Turunan {runId}` membatasi hasil ke keenam akun DU-170-2 sampai DU-170-7 sehingga akun lain di client tidak memengaruhi urutan atau isi hasil; langkah yang tidak memakainya menyatakan sendiri akun yang dicek.

## Test Steps

### Kolom Last Used in Journal dikecualikan dari Search
1. Admin A mengirim permintaan daftar dengan Search `Mar 2026`, periode kolom Last Used in Journal akun `SDD-{runId}`
2. Verifikasi hasil tidak memuat akun `SDD-{runId}`, karena kolom Last Used in Journal dikecualikan dari Search

### Filter atas Used By dan Last Used in Journal
3. Admin A mengirim permintaan daftar dengan Search `Turunan {runId}` dan Filter Function berisi `Asset Cost` serta Filter Used By Min `1`
4. Verifikasi hasil memuat tepat akun `SDD-{runId}`, `SDF-{runId}`, irisan (AND) antar field, dan tidak memuat akun `SDA-{runId}` yang Used By-nya 0
5. Admin A mengirim permintaan daftar dengan Search `Turunan {runId}` dan Filter Used By Min `2` serta Max `10`
6. Verifikasi hasil memuat tepat akun `SDB-{runId}`, `SDD-{runId}`, dengan kedua batas ikut (inklusif)
7. Admin A mengirim permintaan daftar dengan Search `Turunan {runId}` dan Filter Last Used in Journal dari `Jan 2026` sampai `Mar 2026`
8. Verifikasi hasil memuat tepat akun `SDC-{runId}`, `SDD-{runId}`, dengan kedua bulan ikut (inklusif), dan tidak memuat akun `SDA-{runId}`, `SDE-{runId}`, `SDF-{runId}` yang Last Used in Journal-nya kosong

### Sort Used By menurut nilai angka natural
9. Admin A mengirim permintaan daftar dengan Search `Turunan {runId}` dan Sort Used By menaik
10. Verifikasi baris berurutan menurut nilai angka natural (0, 0, 0, 1, 2, 10, bukan 0, 0, 0, 1, 10, 2), dengan akun ber-Used By sama menurut default sort: `SDA-{runId}`, `SDC-{runId}`, `SDE-{runId}`, `SDF-{runId}`, `SDB-{runId}`, `SDD-{runId}`
11. Admin A mengirim permintaan daftar dengan Search `Turunan {runId}` dan Sort Used By menurun
12. Verifikasi baris berurutan `SDD-{runId}`, `SDB-{runId}`, `SDF-{runId}`, `SDA-{runId}`, `SDC-{runId}`, `SDE-{runId}`, dengan akun ber-Used By sama tetap menurut default sort

### Sort Last Used in Journal dengan nilai kosong di akhir saat menaik dan di awal saat menurun
13. Admin A mengirim permintaan daftar dengan Search `Turunan {runId}` dan Sort Last Used in Journal menaik (Oldest First)
14. Verifikasi periode terlama di atas dan akun dengan Last Used in Journal kosong di akhir, akun kosong menurut default sort: `SDB-{runId}`, `SDC-{runId}`, `SDD-{runId}`, `SDA-{runId}`, `SDE-{runId}`, `SDF-{runId}`
15. Admin A mengirim permintaan daftar dengan Search `Turunan {runId}` dan Sort Last Used in Journal menurun (Newest First)
16. Verifikasi akun dengan Last Used in Journal kosong di awal, lalu periode terbaru ke terlama: `SDA-{runId}`, `SDE-{runId}`, `SDF-{runId}`, `SDD-{runId}`, `SDC-{runId}`, `SDB-{runId}`
