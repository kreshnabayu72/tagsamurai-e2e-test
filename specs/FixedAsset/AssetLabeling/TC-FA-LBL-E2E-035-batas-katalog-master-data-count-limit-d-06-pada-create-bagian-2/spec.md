---
id: TC-FA-LBL-E2E-035-batas-katalog-master-data-count-limit-d-06-pada-create-bagian-2
title: "Batas Katalog Master Data Count Limit (D-06) pada Create (bagian 2/2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-101
  - TC-FA-LBL-505
  - TC-FA-LBL-105
coverage:
  web: automated
---

# Batas Katalog Master Data Count Limit (D-06) pada Create (bagian 2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Limit (Pre-setup #11, pengguna `Total Control Limit`; email akun ini tidak tertulis di Pre-setup TC, lihat Temuan untuk QA), password dari `Spectra.env.FA_TC_LIMIT_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_LIMIT_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak mengubah state global kecuali dinyatakan di bawah.
- State global: Master Data Count Limit Company Limit diturunkan ke 1000 (nilai terendah yang diizinkan) di hook `before` dan dipulihkan di hook `after` (S-13: akun atau kemampuan pelaku disediakan tim FE). Suite berjalan serial (`parallel: false`).
- Seeding hook `before`: katalog Company Limit diisi lewat API sampai tepat di batas (seed ini milik spec dan dihapus di `after`).
- Data Pre-setup #14: popup Create/Edit Asset Name tersedia; spec memakai popup Create Asset Name tanpa menyimpannya.
- Kata kunci Search yang tidak cocok: `Zzz No Match 505`.
- Kemampuan teknis (disediakan tim FE/BE, suite.md): sesi API aktor dan fixture BE untuk membaca state katalog dan menyetel serta memulihkan Master Data Count Limit.
- Spec ini tidak membuat label di UI; tidak ada cleanup selain pemulihan seed hook.

## Test Steps

### TC-FA-LBL-101: Klik [+ Label] saat katalog mencapai batas membuka D-06 dan modal Create tidak dibuka

1. Klik `[+ Label]`
2. Verifikasi dialog dengan title `Label Limit Reached` dan body `You've reached the platform limit of [Limit] labels. Contact support if you need a higher limit.` tampil
3. Verifikasi `[Limit]` pada body terisi nilai Master Data Count Limit Company Limit (1000)
4. Verifikasi dialog hanya memiliki satu tombol `[OK]`
5. Verifikasi modal Create Label tidak dibuka
6. Klik `[OK]`
7. Verifikasi hanya dialog yang tertutup

### TC-FA-LBL-505: Klik [+ Label] saat katalog di batas menampilkan D-06 walau hasil Search kosong

8. Ketik Search `Zzz No Match 505`, tekan Enter
9. Verifikasi empty state `No results found` tampil (hasil Search 0 baris)
10. Klik `[+ Label]`
11. Verifikasi dialog dengan title `Label Limit Reached` dan body `You've reached the platform limit of [Limit] labels. Contact support if you need a higher limit.` tampil
12. Verifikasi modal Create Label tidak dibuka, karena jumlah yang dicek adalah total katalog, bukan hasil Search
13. Klik `[OK]`
14. Verifikasi hanya dialog yang tertutup
15. Verifikasi keyword Search `Zzz No Match 505` tetap terisi
16. Klik `(←)` pada kotak Search

### TC-FA-LBL-105: Tombol [➕] pada tab Asset Name saat batas tercapai menampilkan D-06

17. Klik tab `Asset Name`
18. Klik `[+ Asset Name]`
19. Klik tombol `[➕]` pada field Default Label
20. Verifikasi dialog `Label Limit Reached` tampil
21. Verifikasi Modal Create Label tidak dibuka
22. Klik `[OK]`
23. Klik icon `[✕]` pada popup Create Asset Name

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 101, 505, 105. Ketiganya memakai state katalog tepat di batas yang sama dari hook `before`; TC-FA-LBL-105 terakhir karena berpindah ke tab Asset Name (langkah 17).
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 16 (mengosongkan Search), langkah 17 (pindah ke tab Asset Name), langkah 22 (menutup dialog D-06), dan langkah 23 (menutup popup Create Asset Name; form tidak diubah sehingga tidak ada dialog `Unsaved Changes`).
- Skenario ambang (satu di bawah batas, dua di bawah batas, Stay) ada di spec 034 (TC-FA-LBL-102 sampai 104).
- Temuan untuk QA: email dan password akun `Total Control Limit` (Pre-setup #11) tidak tertulis di Pre-setup TC; akun disediakan tim FE (lihat Temuan di spec 034).
