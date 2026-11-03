---
id: TC-FA-LIC-E2E-045-edit-allocation-lewat-ikon-summary-dan-edit
title: "Edit Allocation: Lewat Ikon Summary dan Edit Tanpa Perubahan (No-Op)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-135
  - TC-FA-LIC-136
  - TC-FA-LIC-517
  - TC-FA-LIC-519
coverage:
  web: automated
---

# Edit Allocation: Lewat Ikon Summary dan Edit Tanpa Perubahan (No-Op)

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): hierarki dan alokasi grup dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data: Pre-setup #12: Divisi Logistik beralokasi 500, Kantor Pusat beralokasi 1500 (Used by This Group 700, Allocated to Subgroups 600, Remaining 200), Divisi Keuangan belum beralokasi.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup Pre-setup #12 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Last Updated baris alokasi, entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan baca jumlah entri Changelog Allocation Quota, System Log aktor, dan Activity Log Fixed Asset (audit trail permanen; N dibaca sebelum aksi, asersi memakai selisih terhadap N, S-12): disediakan tim FE/BE lewat fixture BE.

## Test Steps

### TC-FA-LIC-135: Edit tanpa perubahan nilai (No-Op)

1. Klik tab `Allocation Quota`
2. Klik node `Kantor Pusat` di Sidebar
3. Catat jumlah entri Changelog Allocation Quota (baseline TC-FA-LIC-135)
4. Klik tombol ikon `[Edit]` pada baris `Divisi Logistik`
5. Klik `[Save]` tanpa mengubah field
6. Verifikasi modal tertutup
7. Verifikasi toast netral `No changes to save.` (bukan toast sukses)
8. Verifikasi tidak ada error duplikat
9. Verifikasi Allocated Quota baris `Divisi Logistik` tetap `500`
10. Verifikasi jumlah entri Changelog Allocation Quota tidak bertambah dari baseline

### TC-FA-LIC-136: Save dengan field kosong pada grup belum beralokasi

11. Catat jumlah entri Changelog Allocation Quota, System Log aktor, dan Activity Log (baseline TC-FA-LIC-136)
12. Klik tombol ikon `[Edit]` pada baris `Divisi Keuangan`
13. Biarkan field kosong, lalu klik `[Save]`
14. Verifikasi toast netral `No changes to save.`
15. Verifikasi `Divisi Keuangan` tetap `Not Allocated`
16. Verifikasi jumlah entri Changelog Allocation Quota tidak bertambah dari baseline
17. Verifikasi jumlah entri System Log aktor tidak bertambah dari baseline
18. Verifikasi jumlah entri Activity Log tidak bertambah dari baseline

### TC-FA-LIC-517: Edit lewat ikon Edit di samping Total pada Group Quota Summary

19. Pada Group Quota Summary klik tombol ikon `[Edit]` di samping nilai `Total` (1500)
20. Verifikasi Field 1 modal Edit Allocation Quota: `Kantor Pusat (GRP-HQ)`
21. Verifikasi Field 2: `1,300 = 700 assets in this group + 0 reserved + 600 allocated to subgroups`
22. Verifikasi Field 3 ber-pre-fill `1500`
23. Verifikasi helper Field 3: `Available unallocated pool: 200 units.`
24. Isi New Allocated Quota `1550`
25. Klik `[Save]`
26. Verifikasi modal tertutup
27. Verifikasi toast sukses `Success, group license quota updated.`
28. Verifikasi Group Quota Summary Kantor Pusat: Total `1550`, Allocated to Subgroups `600`, Used by This Group `700`, Reserved by This Group `0`, Remaining `250`

### TC-FA-LIC-519: Alokasi pertama lewat ikon Edit di samping tanda strip Total

29. Klik node `Divisi Keuangan` di Sidebar
30. Pada Group Quota Summary klik tombol ikon `[Edit]` di samping `—` pada baris `Total`
31. Verifikasi modal Edit Allocation Quota terbuka dengan Field 3 kosong dan placeholder `Enter allocated quota`
32. Isi New Allocated Quota `50`
33. Klik `[Save]`
34. Verifikasi toast sukses `Success, group license quota updated.`
35. Verifikasi Context Header `Divisi Keuangan (GRP-FIN)` tanpa badge `Not Allocated`
36. Verifikasi Group Quota Summary: Total `50`, Allocated to Subgroups `0`, Used by This Group `0`, Reserved by This Group `0`, Remaining `50`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): klik node Sidebar memilih node blok.
- Urutan TC: TC-FA-LIC-135 dan TC-FA-LIC-136 (no-op, tanpa mutasi) lebih dulu, lalu TC-FA-LIC-517 (Kantor Pusat 1550) dan TC-FA-LIC-519 (Divisi Keuangan 50); tidak ada blok yang bergantung pada nilai yang diubah blok sebelumnya (S-10).
- Pengecualian P-1: klausa `tidak ada entri baru` di `Changelog: Allocation Quota` (TC-FA-LIC-135 c) dan `tidak ada entri log` (TC-FA-LIC-136 b) diasersi di spec ini sebagai jumlah entri yang sama dengan baseline yang dicatat sebelum `[Save]`, karena aksi no-op yang memicunya bergantung pada hierarki dan kuota Pre-setup #12 yang dibangun spec ini dan spec absence log (E2E-111) tidak memuat TC-FA-LIC-135 dan TC-FA-LIC-136. TC-FA-LIC-135 menyebut Changelog saja; TC-FA-LIC-136 tidak menyebut surface log sehingga spec memeriksa Changelog Allocation Quota, System Log aktor, dan Activity Log.
- TC-FA-LIC-517 dan TC-FA-LIC-519 menyimpan alokasi baru; fixture BE pemulih mengembalikannya (hook `after`).
- Alasan di atas 35 langkah (36 langkah): dua blok (TC-135 dan TC-136) satu topik (Edit Allocation lewat ikon) dan berdiri sendiri; langkah di atas 35 berasal dari baseline jumlah entri tiga surface log; kegagalan satu blok tidak membuat blok lain kehilangan makna.
