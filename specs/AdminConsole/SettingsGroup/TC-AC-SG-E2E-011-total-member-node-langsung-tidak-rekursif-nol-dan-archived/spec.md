---
id: TC-AC-SG-E2E-011-total-member-node-langsung-tidak-rekursif-nol-dan-archived
title: "Total Member Node: Active/Suspended Langsung, Tidak Rekursif, Nilai 0 Tetap Link, dan Archived Tidak Dihitung"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-41
  - TC-AC-SG-42
  - TC-AC-SG-43
  - TC-AC-SG-44
coverage:
  web: automated
---

# Total Member Node: Active/Suspended Langsung, Tidak Rekursif, Nilai 0 Tetap Link, dan Archived Tidak Dihitung

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama (TC-AC-SG-41, 42, 44): Total Control Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor kedua (TC-AC-SG-43): Total Control `Distributor Hapus Utama` (Pre-setup #21) `totalControlDistHapus_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_HAPUS_PASSWORD`; dipakai lewat langkah ganti akun. Hook `after` mengembalikan sesi ke akun default suite.
- Nama env `AC_SG_HAPUS_PASSWORD` baru dan perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo (lihat `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite untuk kedua akun UI (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak diubah): `Pohon Uji Utama` entitas Principal (#16) dengan Total Member per node (#19): `Region A` 4, `Branch 2` 3 (`Distributor Epsilon` Active, `Distributor Fajar` Suspended, `Distributor Gunawan` Active), `Region C` 1 (`Distributor Sigma` Active), `Finance Dept` 0; `Distributor Hapus Utama` (#21) dengan node `Hapus Arsip` yang menempel `Client Lama` berstatus Archived. Target aksi hanya dibaca; tidak ada yang diubah.
- Data Dinamis: tidak ada; spec tidak membuat atau mengubah data sehingga tidak ada seeding, suffix `{runId}-011`, maupun cleanup.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-41: Total Member menghitung entitas Active atau Suspended yang di-assign langsung (pohon Principal: Distributor)

1. Ketik Search `Branch 2`, tekan Enter
2. Klik angka Total Member pada baris `Branch 2`
3. Verifikasi popup "Members" untuk `Branch 2` menampilkan 3 entitas bertipe Distributor: `Distributor Epsilon` (Active), `Distributor Fajar` (Suspended), `Distributor Gunawan` (Active)
4. Tutup popup "Members"

### TC-AC-SG-42: Total Member tidak rekursif lintas node dan lintas tipe entitas

5. Ganti isi kotak search dengan `Region A`, tekan Enter
6. Verifikasi sel Total Member baris `Region A` tetap 4 (entitas pada `Branch 1`, `Branch 2`, dan `Room 301` tidak ikut)
7. Ganti isi kotak search dengan `Region C`, tekan Enter
8. Klik angka Total Member pada baris `Region C`
9. Verifikasi popup "Members" `Region C` berisi `Distributor Sigma` saja
10. Tutup popup "Members"

### TC-AC-SG-44: Nilai 0 pada Total Member tetap berupa number link yang membuka popup kosong

11. Ganti isi kotak search dengan `Finance Dept`, tekan Enter
12. Verifikasi sel Total Member baris `Finance Dept` menampilkan "0" (bukan "—")
13. Verifikasi sel Total Member baris `Finance Dept` berupa number link tanpa underline
14. Klik angka 0
15. Verifikasi popup "Members" terbuka dengan teks identitas "Head Office > Finance Dept (0)"
16. Verifikasi popup "Members" menampilkan empty state standar, bukan error
17. Tutup popup "Members"
18. Klik `(←)` pada kotak Search

### TC-AC-SG-43: Entitas berstatus Archived tidak dihitung di Total Member

19. Ganti akun: logout, login sebagai Total Control `Distributor Hapus Utama` (`totalControlDistHapus_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_SG_HAPUS_PASSWORD`)
20. Buka halaman `Settings > Group` lewat sidebar
21. Ketik Search `Hapus Arsip`, tekan Enter
22. Verifikasi sel Total Member baris `Hapus Arsip` bernilai 0 walau `Client Lama` (Archived) menempel di node itu
23. Klik angka Total Member pada baris `Hapus Arsip`
24. Verifikasi popup "Members" terbuka dengan empty state standar tanpa baris
25. Tutup popup "Members"
26. Klik `(←)` pada kotak Search

## Notes

- Urutan TC di spec: TC-AC-SG-41, 42, 44, lalu 43 supaya semua blok akun pertama berurutan dan ganti akun terjadi sekali di akhir (S-07, S-10).
- Langkah penghubung (S-03, R-16): langkah 1, 5, 7, 11, 21 (Search untuk menemukan baris target karena tabel All Groups terbagi dua halaman), langkah 4, 10, 17, 25 (menutup popup), langkah 18 dan 26 (mengosongkan Search), langkah 19 dan 20 (ganti akun dan membuka halaman sebagai akun kedua).
- Langkah 9 memakai klausa "saja" pada Expected b TC-AC-SG-42 sebagai padanan pernyataan bahwa Partner dan Client di jaringan `Distributor Gamma` tidak ikut terhitung; anchor positifnya adalah baris `Distributor Sigma` pada popup yang sama.
- Temuan untuk QA:
  - TC-AC-SG-41 Expected tidak menyebut kolom popup selain nama, tipe, dan status; spec mengasersi tiga entitas dengan tipe dan status sebagaimana tertulis.
  - TC-AC-SG-44 langkah 2 hanya menyebut "perhatikan sel"; Expected a diasersi sebagai dua klausa (nilai "0" dan number link tanpa underline).
