---
id: TC-GS-IMPORT-E2E-101-combobox-represented-by-client-a-minimal-2-karakter-pencocokan-email
title: "Combobox Represented By (Client A): minimal 2 karakter, pencocokan email atau nama, maksimum 10 saran berurut, eligibility"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-898
  - TC-GS-IMPORT-964
  - TC-GS-IMPORT-965
  - TC-GS-IMPORT-966
coverage:
  web: automated
---

# Combobox Represented By (Client A): minimal 2 karakter, pencocokan email atau nama, maksimum 10 saran berurut, eligibility

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > User Non Login untuk Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Pre-setup Client A (tidak diubah): User Login aktif `budi.manager@example.com`; User Non Login `agus.nonlogin@example.com`.
- Data Dinamis: D-06 (Draft User Non Login 5 baris `pending` dari `user-non-login-5.csv`), dipulihkan oleh hook `beforeEach` (Kontrak Fixture R2); D-92 (12 User Login aktif Activated di Client A: email `lookup-01@example.com` sampai `lookup-12@example.com`, First Name `Pemilik`, Last Name `01` sampai `12`; dibuat lewat skrip fixture di hook `before` dan dihapus di hook `after`; nama dan email literal karena asersi bergantung pada pencocokan dan urutan; pengecualian S-12 dengan seeding idempotent dan suite serial). Nilai ketikan: `b`, `bu`, `LOOKUP-03`, `pemilik 07`, `lookup`, `lookup-1`, `tidak.ada`, `agus`, `budi`.
- Kemampuan teknis: pengamatan panel saran combobox dan label saran, skrip seed D-92 dan pemulihan draft D-06 (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain draft Client A, user D-92, dan flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus 12 User Login D-92, pulihkan draft Client A ke D-06, lepas kunci sesi edit.

## Test Steps

### TC-GS-IMPORT-964, 965, 966: Panel saran (satu sesi edit)

1. Klik `⋯` pada baris #1, pilih `Edit`
2. Klik sel Represented By baris #1 tanpa mengetik
3. Verifikasi tidak ada daftar saran
4. Verifikasi tidak ada email User yang ditampilkan
5. Ketik `b`
6. Verifikasi daftar saran tidak tampil
7. Ketik `u` sehingga teks menjadi `bu`
8. Verifikasi daftar saran tampil
9. Verifikasi daftar saran memuat `budi.manager@example.com`
10. Hapus teks lalu ketik `LOOKUP-03`
11. Verifikasi daftar saran memuat tepat satu saran berlabel `lookup-03@example.com` (cocok pada email, huruf besar-kecil diabaikan)
12. Hapus teks lalu ketik `pemilik 07`
13. Verifikasi daftar saran memuat tepat satu saran berlabel `lookup-07@example.com` (cocok pada nama lengkap `Pemilik 07`)
14. Verifikasi nama `Pemilik 07` tidak dipakai sebagai label saran
15. Pilih saran yang tampil
16. Verifikasi sel Represented By menampilkan `lookup-07@example.com`
17. Hapus teks lalu ketik `lookup`
18. Verifikasi daftar saran memuat tepat 10 saran urut `lookup-01@example.com` sampai `lookup-10@example.com`
19. Verifikasi `lookup-11@example.com` dan `lookup-12@example.com` tidak tampil
20. Hapus teks lalu ketik `lookup-1`
21. Verifikasi daftar saran memuat tepat 3 saran urut `lookup-10@example.com`, `lookup-11@example.com`, `lookup-12@example.com`
22. Klik `[Cancel]`, lalu klik `[Discard]` pada dialog Discard Changes

### TC-GS-IMPORT-898: Hanya User Login eligible tanpa teks bebas

23. Klik `⋯` pada baris #1, pilih `Edit`
24. Klik sel Represented By baris #1 dan ketik `tidak.ada`
25. Verifikasi daftar saran kosong
26. Verifikasi tidak ada pilihan `Use "tidak.ada"`
27. Hapus teks lalu ketik `agus`
28. Verifikasi daftar saran tidak memuat `agus.nonlogin@example.com` (bukan User Login eligible)
29. Hapus teks lalu ketik `budi`
30. Pilih saran `budi.manager@example.com`
31. Verifikasi sel menampilkan `budi.manager@example.com` sebagai label email
32. Klik `[Save]`
33. Verifikasi muncul toast sukses: "Success, row has been updated."
34. Verifikasi baris #1 berstatus `pending`
35. Verifikasi Represented By baris #1 `budi.manager@example.com`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional (seed 12 user D-92 hanya data; di bawah ambang kelas e).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penggabungan: TC-964, TC-965, dan TC-966 berbagi satu sesi edit pada sel Represented By yang sama; sel dikosongkan di antara kasus (hapus teks) tanpa membuka ulang sesi (halaman yang dipakai berulang, bagian 3). TC-898 menyimpan perubahan sehingga dijalankan paling akhir.
- Langkah penghubung (tanpa `Verifikasi`): langkah 22 membuang perubahan (nilai `lookup-07@example.com` dipilih pada langkah 15).
- Spec berisi 35 langkah.
- Pembagian TC lintas spec: TC-GS-IMPORT-676, 967, 968 (combobox Client C) ada di spec 102; TC-GS-IMPORT-969 di spec lain.
- Temuan untuk QA:
  - TC-GS-IMPORT-965 Langkah 7 ("Pilih saran yang tampil") tidak menyebut urutan hasil bila lebih dari satu; Expected a menyebut tepat satu saran sehingga tidak ambigu.
  - Post Condition semua TC ("Draft Client A dipulihkan ke D-06 dan 12 User Login D-92 dihapus") adalah pemulihan oleh fixture dan dikerjakan hook `after`; tidak diasersi (S-01).
