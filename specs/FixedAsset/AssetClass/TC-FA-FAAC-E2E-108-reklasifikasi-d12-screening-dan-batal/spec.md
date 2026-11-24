---
id: TC-FA-FAAC-E2E-108-reklasifikasi-d12-screening-dan-batal
title: "Reklasifikasi D-12: Dialog Reclassify Balances, Cancel, Dua Akun, dan Perubahan Tanpa Dialog"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-344
  - TC-FA-FAAC-347
  - TC-FA-FAAC-348
  - TC-FA-FAAC-349
sourceRules: ["D-12", "F-FAAC-02.k9d", "§4.2f#b2", "FAAC-LOGIC-06a", "F-FAAC-02.k18"]
smoke: []
dependsOn: []
trace:
  "D-12": [7, 8, 21, 22]
  "F-FAAC-02.k9d": [10, 11, 17, 18]
  "§4.2f#b2": [13, 25]
  "FAAC-LOGIC-06a": [30, 34, 38]
  "F-FAAC-02.k18": [30, 34, 38]
coverage:
  web: automated
---

# Reklasifikasi D-12: Dialog Reclassify Balances, Cancel, Dua Akun, dan Perubahan Tanpa Dialog

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nilai literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-EXP` dengan Last Exported Period Aug 2026 dan akun lengkap: Asset Cost `11001 – Machinery Cost`, Accumulated Depreciation `12001 – Accumulated Depreciation Machinery` (seed Pre-setup sesuai NC-16), tanpa aset aktif sehingga perubahan akun tidak memicu dialog `Apply Changes`. Akun pengganti tersedia di dropdown: `11002 – Machinery Cost Alt`, `12002 – Accumulated Depreciation Other`, dan satu akun Depreciation Expense lain yang ditetapkan fixture.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: akun Depreciation Expense dan Asset Cost `B-EXP` dikembalikan ke nilai seed (TC-349 menyimpan perubahan akun).
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode dan nomor akun itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Reload tidak dipakai pada form yang terisi; penutupan form mengikuti S-08 (breadcrumb `Asset Class`, `Unsaved Changes`, `[Leave]`).
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): jumlah entri Changelog Asset Class dibaca tepat sebelum aksi pemicu tiap TC yang mengasersi "tanpa log" (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-344: Mengubah akun Asset Cost menampilkan dialog Reclassify Balances

1. Ketik Search `B-EXP`, tekan Enter
2. Klik link Class Code `B-EXP` di tabel
3. Klik tab `Accounts`
4. Ganti Asset Cost menjadi `11002 – Machinery Cost Alt`
5. Catat jumlah entri Changelog Asset Class (Nc) sebagai baseline lewat kemampuan baca log
6. Klik `Save`
7. Verifikasi Dialog `Reclassify Balances` memuat bullet `Asset Cost: 11001 – Machinery Cost → 11002 – Machinery Cost Alt` dan teks `Balances of this asset class are still recorded in the old account. Create a reclassification journal to the new account?`
8. Verifikasi tombol `Cancel`, `New journals only`, dan `Create reclassification`

### TC-FA-FAAC-347: Cancel pada D-12 tidak menyimpan apa pun

9. Klik `Cancel`
10. Verifikasi dialog menutup
11. Verifikasi halaman Detail tetap terbuka
12. Klik breadcrumb `Asset Class`
13. Verifikasi dialog `Unsaved Changes` tampil
14. Klik `[Leave]`
15. Klik link Class Code `B-EXP` di tabel
16. Klik tab `Accounts`
17. Verifikasi akun tidak berubah di server: Asset Cost tetap `11001 – Machinery Cost`
18. Verifikasi jumlah entri Changelog Asset Class sama dengan Nc (tidak ada entri baru)

### TC-FA-FAAC-348: Mengubah Asset Cost dan Accumulated Depreciation menampilkan dua bullet dan teks jamak

19. Ganti Asset Cost menjadi `11002 – Machinery Cost Alt` dan Accumulated Depreciation menjadi `12002 – Accumulated Depreciation Other`
20. Klik `Save`
21. Verifikasi dua bullet `Asset Cost: 11001 – Machinery Cost → 11002 – Machinery Cost Alt` dan `Accumulated Depreciation: 12001 – Accumulated Depreciation Machinery → 12002 – Accumulated Depreciation Other`
22. Verifikasi teks `Balances of this asset class are still recorded in the old accounts. Create reclassification journals to the new accounts?`
23. Klik `Cancel`
24. Klik breadcrumb `Asset Class`
25. Verifikasi dialog `Unsaved Changes` tampil
26. Klik `[Leave]`

### TC-FA-FAAC-349: D-12 tidak tampil untuk perubahan Depreciation Expense, Gain, Loss, mengosongkan, atau mengisi akun kosong

27. Klik link Class Code `B-EXP` di tabel
28. Klik tab `Accounts`
29. Ganti Depreciation Expense menjadi akun lain, lalu klik `Save`
30. Verifikasi Save tersimpan langsung tanpa dialog `Reclassify Balances` dan tanpa permintaan jurnal reklasifikasi (halaman kembali ke tabel Asset Class)
31. Klik link Class Code `B-EXP` di tabel
32. Klik tab `Accounts`
33. Kosongkan Asset Cost, lalu klik `Save`
34. Verifikasi Save tersimpan langsung tanpa dialog `Reclassify Balances` dan tanpa permintaan jurnal reklasifikasi (halaman kembali ke tabel Asset Class)
35. Klik link Class Code `B-EXP` di tabel
36. Klik tab `Accounts`
37. Isi Asset Cost kembali dari kosong dengan `11001 – Machinery Cost`, lalu klik `Save`
38. Verifikasi Save tersimpan langsung tanpa dialog `Reclassify Balances` dan tanpa permintaan jurnal reklasifikasi (halaman kembali ke tabel Asset Class)
39. Klik `(←)` pada kotak Search

## Notes

1. Urutan dalam spec: dialog dan Cancel (TC-344, TC-347) lebih dulu, dua akun (TC-348), dan TC-349 yang menyimpan perubahan akun di akhir. Sesi edit pertama dibuka sekali di langkah 2 dan 3 untuk TC-344 dan TC-347; langkah TC-347 "Save lalu Cancel" identik dengan langkah 4 dan 6 TC-344 (langkah 5 mencatat baseline Changelog TC-347 sebelum Save itu) sehingga Cancel dilakukan pada dialog yang sama.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (Search untuk menemukan baris target, R-16), langkah 5 (baseline Changelog, S-12), langkah 12 sampai 14 dan 24 sampai 26 (menutup form yang terisi lewat breadcrumb `Asset Class`, `Unsaved Changes`, dan `[Leave]`, S-08 dan S-09), langkah 15 dan 16 (membuka Detail kembali untuk membaca akun di server karena reload tidak dipakai pada form terisi), dan langkah 39 (mengosongkan Search).
3. Alasan melebihi sekitar 35 langkah (39 langkah): spec berisi empat blok TC yang berdiri sendiri pada dialog D-12 yang sama; blok TC-349 mengulang tiga kali pola Save yang sama dengan akun berbeda (langkah 27 sampai 38) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
4. S-05 dan P-1: Expected "tidak ada log" pada TC-347 diasersi di spec ini (langkah 18) dengan `Verifikasi` selisih jumlah entri Changelog Asset Class terhadap baseline (langkah 5); aksinya bukan request langsung (kelas a). TC tidak menyebut surface log selain "log"; yang diasersi Changelog Asset Class.
5. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal dengan nomor akun tertentu; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
6. Temuan untuk QA: TC-349 Expected tidak menyebut indikator tersimpan; spec memakai perilaku Save yang kembali ke tabel seperti pada TC-345 dan TC-346. TC-349 tidak menyebut akun pengganti Depreciation Expense atau nilai Asset Cost yang diisi kembali; spec memakai akun lain dari fixture dan `11001 – Machinery Cost`. Klausa "tanpa permintaan jurnal reklasifikasi" tidak punya cara observasi di UI Asset Class (jurnal reklasifikasi diuji di Export Journal, FAEJ-LOGIC-09) dan diasersi sebagai tidak adanya dialog.
