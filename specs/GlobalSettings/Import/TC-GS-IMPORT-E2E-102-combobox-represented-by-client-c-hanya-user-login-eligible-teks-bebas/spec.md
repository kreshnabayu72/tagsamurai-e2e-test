---
id: TC-GS-IMPORT-E2E-102-combobox-represented-by-client-c-hanya-user-login-eligible-teks-bebas
title: "Combobox Represented By (Client C): hanya User Login eligible, teks bebas tidak menjadi nilai, nilai tersimpan tidak ditemukan memblokir Save"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-676
  - TC-GS-IMPORT-967
  - TC-GS-IMPORT-968
coverage:
  web: automated
---

# Combobox Represented By (Client C): hanya User Login eligible, teks bebas tidak menjadi nilai, nilai tersimpan tidak ditemukan memblokir Save

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > User Non Login untuk Client C.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Pre-setup Client C (tidak diubah): User Login `rina.admin.c@example.com` (Activated), `budi.manager.c@example.com` (Activated), `tono.inactive.c@example.com` (Inactive), `baru.impor.c@example.com` (Pending Activation); User Non Login `agus.nonlogin.c@example.com`.
- Data Dinamis: D-90 (Draft User Non Login Client C 1 baris `error` dari `user-non-login-rep-invalid.csv`: Siti Rahayu, `siti.rahayu@example.com`, Division `Engineering`, Position kosong, Represented By `tidak.ada@example.com`; pesan baris "Represented by must be an active User Login account"), dibuat lewat skrip fixture dan dipulihkan sebelum spec (Kontrak Fixture R2). Nilai ketikan: `tono.inactive`, `baru.impor`, `agus.nonlogin`, `rina.admin.c`, `budi.manager.c@example.com`, `budi`.
- Kemampuan teknis: pengamatan panel saran combobox, tombol Esc, skrip pemulihan draft D-90 (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain draft Client C dan flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): buang draft User Non Login Client C dan lepas kunci sesi edit.

## Test Steps

### TC-GS-IMPORT-676, 967, 968: Satu sesi edit pada sel Represented By tersimpan tidak ditemukan

1. Muat ulang halaman Import > User Non Login
2. Klik `⋯` pada baris #1, pilih `Edit`
3. Verifikasi sel Represented By baris #1 menampilkan `tidak.ada@example.com` sebagai nilai terpilih berstatus Invalid (ikon dan teks deskriptif) dan tidak dikosongkan
4. Klik sel Represented By baris #1 dan ketik `tono.inactive`
5. Verifikasi tidak ada saran
6. Verifikasi tidak ada pilihan `Use "tono.inactive"`
7. Hapus teks lalu ketik `baru.impor`
8. Verifikasi tidak ada saran
9. Verifikasi tidak ada pilihan `Use "baru.impor"`
10. Hapus teks lalu ketik `agus.nonlogin`
11. Verifikasi tidak ada saran
12. Verifikasi tidak ada pilihan `Use "agus.nonlogin"`
13. Hapus teks lalu ketik `rina.admin.c`
14. Verifikasi daftar saran memuat `rina.admin.c@example.com`
15. Hapus teks lalu ketik `budi.manager.c@example.com` lengkap
16. Tekan Esc untuk menutup panel tanpa memilih saran
17. Verifikasi sel Represented By menampilkan `tidak.ada@example.com` sebagai nilai terpilih berstatus Invalid
18. Verifikasi teks yang diketik tidak menjadi nilai sel
19. Klik `[Save]` tanpa mengubah sel Represented By
20. Verifikasi `[Save]` diblokir tanpa toast sukses
21. Verifikasi sel Represented By berborder `danger` dengan pesan "Represented by must be an active User Login account"
22. Verifikasi footer tetap menampilkan `[Cancel]` dan `[Save]`
23. Verifikasi Error Summary Callout memuat baris pesan "Represented by must be an active User Login account" dengan badge "1 row"
24. Ketik `budi` pada sel Represented By, lalu pilih saran `budi.manager.c@example.com`
25. Klik `[Save]`
26. Verifikasi muncul toast sukses: "Success, row has been updated."
27. Verifikasi baris #1 berstatus `pending`
28. Verifikasi baris #1 Represented By `budi.manager.c@example.com`
29. Verifikasi footer `[Import (1)]` tampil kembali

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penggabungan: TC-967, TC-968, dan TC-676 berbagi satu sesi edit pada draft D-90 yang sama; asersi TC-676 a pada langkah 3, TC-967 pada langkah 4 sampai 14, TC-968 a pada langkah 15 sampai 18, TC-968 b dan TC-676 b-c pada langkah 19 sampai 23, TC-676 d pada langkah 24 sampai 29. Teks diketik lalu dihapus di antara kasus tanpa membuka ulang sesi (halaman yang dipakai berulang, bagian 3).
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 (muat ulang halaman, Langkah 1 TC-676).
- Spec berisi 29 langkah.
- Pembagian TC lintas spec: TC-GS-IMPORT-898, 964 sampai 966 (combobox Client A) ada di spec 101.
- Temuan untuk QA:
  - TC-GS-IMPORT-967 Expected a menyebut "tidak ada pilihan `Use "[Value]"`" tanpa menyebut pesan kosong lain; spec memecah per nilai (langkah 5 sampai 12).
  - TC-GS-IMPORT-676 Post Condition ("Draft ... berisi 1 baris `pending`") sudah diasersi pada Expected d; Post Condition TC-967 dan 968 ("Draft Client C dipulihkan ke D-90") dikerjakan hook dan tidak diasersi (S-01).
