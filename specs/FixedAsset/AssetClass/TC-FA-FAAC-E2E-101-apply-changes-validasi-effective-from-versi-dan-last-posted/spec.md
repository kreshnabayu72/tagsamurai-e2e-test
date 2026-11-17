---
id: TC-FA-FAAC-E2E-101-apply-changes-validasi-effective-from-versi-dan-last-posted
title: "Apply Changes: Validasi Effective From terhadap Last Posted Period dan Versi Terakhir"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-319
  - TC-FA-FAAC-320
sourceRules: ["V-25", "FAAC-LOGIC-07b", "F-FAAC-02.k8", "F-FAAC-02.k18", "FAAC-LOGIC-07a"]
smoke: []
dependsOn: []
trace:
  "V-25": [7, 20]
  "FAAC-LOGIC-07b": [7, 11, 24]
  "F-FAAC-02.k8": [9, 22]
  "F-FAAC-02.k18": [13, 26]
  "FAAC-LOGIC-07a": 28
coverage:
  web: automated
---

# Apply Changes: Validasi Effective From terhadap Last Posted Period dan Versi Terakhir

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-LPP` dipakai aset (1 Asset Name dengan aset aktif), Last Posted Period tiga bulan sebelum bulan berjalan M (M-3; mis. Jul 2026 bila M = Oct 2026), versi terakhir berlaku sejak Jan 2026 (seed Pre-setup sesuai NC-16); Asset Class `B-VLAST` dipakai aset, belum pernah diposting, versi terakhir berlaku sejak M-2. Accounting Period M-1 berstatus Closed; M-2 dan M-3 berstatus Open (seed periode relatif bulan berjalan).
- Jam: bulan berjalan M mengikuti zona waktu General Settings client (NC-11); jam server dan jam browser sinkron dan tidak digeser spec ini.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: versi baru Useful Life 48 pada `B-LPP` dan `B-VLAST` dihapus dan nilai awal dipulihkan.
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode dan periode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-319: Effective From pada atau sebelum Last Posted Period ditolak V-25

1. Ketik Search `B-LPP`, tekan Enter
2. Klik link Class Code `B-LPP` di tabel
3. Klik tab `Depreciation`
4. Ubah Useful Life menjadi 48
5. Klik `Save`
6. Pilih Effective From sama dengan Last Posted Period (M-3; mis. `Jul 2026` bila M = Oct 2026)
7. Verifikasi caption `Effective from must not be earlier than [MMM YYYY]` dengan bulan = M-2 (mis. `Aug 2026` bila M = Oct 2026)
8. Klik `Apply`
9. Verifikasi `Apply` tidak menyimpan (dialog `Apply Changes` tetap terbuka)
10. Pilih Effective From satu bulan setelahnya (M-2; mis. `Aug 2026` bila M = Oct 2026)
11. Verifikasi tidak ada caption untuk Effective From M-2 (tepat satu bulan setelah Last Posted Period)
12. Klik `Apply`
13. Verifikasi `Apply` berhasil (perubahan tersimpan dan dialog `Apply Changes` tertutup)

### TC-FA-FAAC-320: Effective From lebih awal dari versi terakhir ditolak, sama dengan versi terakhir diizinkan

14. Ganti isi kotak search dengan `B-VLAST`, tekan Enter
15. Klik link Class Code `B-VLAST` di tabel
16. Klik tab `Depreciation`
17. Ubah Useful Life menjadi 48
18. Klik `Save`
19. Pilih Effective From satu bulan sebelum Effective From versi terakhir (M-3; mis. `Jul 2026` bila M = Oct 2026)
20. Verifikasi caption `Effective from must not be earlier than [MMM YYYY]` dengan bulan = Effective From versi terakhir (M-2, ditulis MMM YYYY; mis. `Aug 2026` bila M = Oct 2026)
21. Klik `Apply`
22. Verifikasi `Apply` tidak menyimpan (dialog `Apply Changes` tetap terbuka)
23. Pilih Effective From sama dengan Effective From versi terakhir (M-2)
24. Verifikasi tidak ada caption untuk Effective From M-2
25. Klik `Apply`
26. Verifikasi `Apply` berhasil (perubahan tersimpan dan dialog `Apply Changes` tertutup)
27. Buka Detail `B-VLAST` dan klik tab `Depreciation`
28. Verifikasi Useful Life 48 berlaku (versi yang dibuat belakangan yang berlaku)
29. Klik breadcrumb `Asset Class`
30. Klik `(←)` pada kotak Search

## Notes

1. Urutan dalam spec: validasi yang ditolak lebih dulu pada tiap TC, lalu Apply yang berhasil; kedua TC memakai Asset Class berbeda sehingga masing-masing membuka Detail sekali.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 dan 14 (Search untuk menemukan baris target, R-16), langkah 27 (membuka Detail untuk membaca versi berlaku), langkah 29 (kembali ke tabel), dan langkah 30 (mengosongkan Search).
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal dengan periode tertentu; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. Temuan untuk QA: TC-319 dan TC-320 memakai bulan relatif terhadap bulan berjalan M (M-1 Closed, M-2 dan M-3 Open; Last Posted Period `B-LPP` = M-3, versi terakhir `B-VLAST` sejak M-2); contoh bulan di spec hanya ilustrasi bila M = Oct 2026, dan asersi memakai bulan hasil hitung dari M. Langkah 13 dan 26 mengasersi Apply berhasil tanpa teks toast karena Expected TC-319 b dan TC-320 b tidak menyebutnya. Expected TC-320 b "versi yang dibuat belakangan yang berlaku" tidak menyebut cara observasi; spec memakai nilai Useful Life 48 pada Detail.
