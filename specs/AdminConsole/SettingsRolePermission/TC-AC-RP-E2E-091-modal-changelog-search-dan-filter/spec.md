---
id: TC-AC-RP-E2E-091-modal-changelog-search-dan-filter
title: "Modal Changelog: Search dan Filter Date, Action, Modified By, Field, Object"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-302
  - TC-AC-RP-303
  - TC-AC-RP-304
  - TC-AC-RP-305
coverage:
  web: automated
---

# Modal Changelog: Search dan Filter Date, Action, Modified By, Field, Object

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Hook suite (flag Guided Tooltip halaman ini, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: #11 (tree group Principal), #12 (user Standard), #13 (pemegang Total Control dan Read Only), #15 (penugasan peran individual), dan #18 (riwayat Changelog seed). Seed Changelog Pre-setup #18 memuat entri `Auto-Revert`, `Remove`, dan entri bertanggal 05 Jun 2026 sampai 08 Jun 2026 dengan Modified By "Bambang H", entri Add/Remove Additional Approver pada Tab System, dan entri Object `Fajar Nugroho` pada Tab Group Manager; kolom Action, Modified By, dan Object memuat sedikitnya dua nilai berbeda. Hasil Search dan Filter diamati pada halaman pertama (Pagination default 10).
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada data Dinamis bersuffix `+{runId}-<NNN>` dan tidak ada seeding. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-302: Search Changelog mencakup Action, Object, Field, Old Value, New Value, Modified By

1. Klik ikon Changelog
2. Ketik Search "auto-revert", tekan Enter
3. Verifikasi sedikitnya satu baris tampil
4. Verifikasi seluruh baris hasil Search ber-Action `Auto-Revert`
5. Ganti isi kotak search dengan "16 Jun", tekan Enter
6. Verifikasi empty state "No results found" tampil karena kolom Date tidak Searchable
7. Klik `(←)` pada kotak Search

### TC-AC-RP-303: Filter Changelog Date, Action, Modified By

8. Klik Filter
9. Verifikasi field Filter: Date ("Select date"), Action ("All actions"), User ("All users"), dan Modified By ("All users")
10. Verifikasi tidak ada field Field pada varian Total Control
11. Pilih Action "Remove", klik `[Apply]`
12. Verifikasi sedikitnya satu baris tampil
13. Verifikasi seluruh baris hasil Filter ber-Action `Remove`
14. Klik Filter, lalu klik `[Clear Field]`
15. Pilih Date 05 Jun 2026 sampai 08 Jun 2026 dan Modified By "Bambang H", klik `[Apply]`
16. Verifikasi sedikitnya satu baris tampil
17. Verifikasi seluruh baris hasil Filter berada pada 05 Jun 2026 sampai 08 Jun 2026 dengan Modified By "Bambang H"
18. Klik Filter, klik `[Clear Field]`, lalu tutup panel Filter
19. Tutup modal Changelog

### TC-AC-RP-304: Filter Field hanya tersedia pada varian System dan Detail Role

20. Klik tab `System`
21. Klik ikon Changelog
22. Klik Filter
23. Verifikasi field Filter memuat "Field" ("All fields")
24. Pilih Field "Additional Approver", klik `[Apply]`
25. Verifikasi sedikitnya satu baris tampil
26. Verifikasi seluruh baris hasil Filter adalah entri Add atau Remove Additional Approver
27. Klik Filter, klik `[Clear Field]`, lalu tutup panel Filter
28. Tutup modal Changelog

### TC-AC-RP-305: Filter Object Changelog

29. Klik tab `Group Manager`
30. Klik ikon Changelog
31. Klik Filter
32. Verifikasi field filter kolom Object berlabel "User" dengan placeholder "All users"
33. Pilih satu nilai Object `Fajar Nugroho`, klik `[Apply]`
34. Verifikasi sedikitnya satu baris tampil
35. Verifikasi seluruh baris hasil Filter adalah entri milik `Fajar Nugroho`
36. Klik Filter, klik `[Clear Field]`, lalu tutup panel Filter
37. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09): langkah 7, 14, 18, 19, 27, 28, 36, 37.
- Search "16 Jun" memakai empty state "No results found" sebagai anchor positif yang sah untuk hasil Search kosong (bagian 8b butir 2); Search pertama "auto-revert" didahului Verifikasi sedikitnya satu baris sebagai pembanding asersi universal.
- Ganti isi kotak search dan pengosongan Search mengikuti bagian 8b butir 9; Filter, `[Clear Field]`, dan penutupan panel Filter adalah langkah penghubung supaya blok berikutnya tidak mewarisi filter (S-09).
- Asersi universal atas hasil Filter dan Search diamati pada halaman pertama (S-14).
- Alasan sekitar 35 langkah (37 langkah): empat blok Search dan Filter satu kelas fungsional pada modal Changelog yang sama, hanya membaca, dan tiap blok berdiri sendiri (varian tab dan filter berbeda); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-RP-305 tidak menyebut nilai Object yang dipilih; spec memakai `Fajar Nugroho` (penugasan GM Pre-setup #14).
  - TC-AC-RP-304 Expected "hasil hanya entri Add/Remove Additional Approver" bergantung pada seed Pre-setup #18 yang memuat entri Additional Approver; seed disediakan tim FE/BE.
