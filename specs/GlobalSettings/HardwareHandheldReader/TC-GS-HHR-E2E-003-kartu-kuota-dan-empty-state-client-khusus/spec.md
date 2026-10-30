---
id: TC-GS-HHR-E2E-003-kartu-kuota-dan-empty-state-client-khusus
title: "License Counter Cards Used of Kuota dan Remaining, Kartu Kuota Habis Client Q, dan Empty State Client E"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-15
  - TC-GS-HHR-16
  - TC-GS-HHR-17
coverage:
  web: automated
---

# License Counter Cards Used of Kuota dan Remaining, Kartu Kuota Habis Client Q, dan Empty State Client E

## Prerequisites

- Mode: FE+BE (backend nyata). Suite `parallel: false`.
- Akun aktor:
  - Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1, Client A) untuk TC-GS-HHR-15. Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`.
  - Total Control Client Q `totalControl_automated_{namaClient}@qwertysystem.net` dengan nama client Client Q, untuk TC-GS-HHR-16: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_CLIENTQ_TC_PASSWORD` (env baru bila belum terdaftar; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`).
  - Total Control Client E `totalControl_automated_{namaClient}@qwertysystem.net` dengan nama client Client E, untuk TC-GS-HHR-17: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_CLIENTE_TC_PASSWORD` (env baru bila belum terdaftar; didaftarkan seperti di atas).
  - Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun Total Control Client A default suite.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Hardware > Handheld Reader untuk akun Total Control Client A; setelah ganti akun, halaman dibuka lewat langkah eksplisit.
- Guided Tooltip: flag halaman Handheld Reader (`guided_tooltip_seen_gs-handheld-reader`) mengikuti hook suite (lihat `suite.md`), termasuk akun Client Q dan Client E (disediakan tim FE).
- Data Pre-setup (tidak diubah spec ini, hanya dibaca):
  - Client A (plan Growth, alokasi `Short Range` 8 dan `Long Range` 6): Seed Reader A (DD-01 s.d. DD-10) dipulihkan fixture backend (disediakan tim FE) sebelum spec berjalan. Status reader: DD-01, DD-03, DD-05, DD-07, DD-09 berjenis Long Range (DD-01 Available, DD-03 Damaged, DD-05 Waiting for Approval, DD-07 Available, DD-09 Available); DD-02, DD-04, DD-06, DD-08, DD-10 berjenis Short Range (DD-02 Available, DD-04 Missing, DD-06 Available, DD-08 Available, DD-10 Waiting for Approval).
  - Client Q: `Short Range` 2 dari 2 dan `Long Range` 3 dari 3 terpakai (0 remaining).
  - Client E: belum memiliki reader, entri Changelog, maupun Event Log; alokasi `Short Range` 2 dan `Long Range` 2.
- Data Dinamis: tidak ada.
- Kemampuan teknis: ganti akun antar client (logout lalu login); pembacaan teks kartu.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`) dan sesi akun (dipulihkan hook `after`).

## Test Steps

### TC-GS-HHR-15: License Counter Cards menampilkan Used of kuota dan Available remaining (Client A)

1. Amati dua License Counter Card
2. Verifikasi kartu berjudul `Short Range` (tanpa kata License) menampilkan nilai utama `5 of 8`
3. Verifikasi kartu `Short Range` menampilkan keterangan `3 remaining`
4. Verifikasi kartu berjudul `Long Range` (tanpa kata License) menampilkan nilai utama `5 of 6`
5. Verifikasi kartu `Long Range` menampilkan keterangan `1 remaining`
6. Verifikasi nilai Used kedua kartu menghitung reader berstatus Available, Damaged, Missing, dan Waiting for Approval: `Short Range` 5 reader (DD-02 dan DD-06 dan DD-08 Available, DD-04 Missing, DD-10 Waiting for Approval) dan `Long Range` 5 reader (DD-01 dan DD-07 dan DD-09 Available, DD-03 Damaged, DD-05 Waiting for Approval)

### TC-GS-HHR-16: Kartu kuota habis menampilkan 0 remaining pada Client Q

7. Ganti akun: logout dari akun Total Control Client A
8. Login sebagai Total Control Client Q dengan `Spectra.env.GS_CLIENTQ_TC_PASSWORD`
9. Buka Global Settings > Hardware > Handheld Reader
10. Amati dua License Counter Card
11. Verifikasi kartu `Short Range` menampilkan `2 of 2`
12. Verifikasi kartu `Short Range` menampilkan `0 remaining`
13. Verifikasi kartu `Long Range` menampilkan `3 of 3`
14. Verifikasi kartu `Long Range` menampilkan `0 remaining`

### TC-GS-HHR-17: Empty state saat Client belum memiliki reader (Client E)

15. Ganti akun: logout dari akun Total Control Client Q
16. Login sebagai Total Control Client E dengan `Spectra.env.GS_CLIENTE_TC_PASSWORD`
17. Buka Global Settings > Hardware > Handheld Reader
18. Amati area tabel
19. Verifikasi ilustrasi tampil menggantikan tabel dengan judul `No handheld reader yet`
20. Verifikasi deskripsi empty state `Get started by creating your first handheld reader.`
21. Verifikasi tidak ada tombol aksi pada empty state
22. Verifikasi tombol `[+ Activate Reader]` ada di toolbar
23. Verifikasi License Counter Cards tetap tampil
24. Verifikasi kartu `Short Range` menampilkan `0 of 2` dan `2 remaining`
25. Verifikasi kartu `Long Range` menampilkan `0 of 2` dan `2 remaining`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 15, 16, 17. Akun default suite (Client A) lebih dulu; TC-GS-HHR-16 dan 17 masing-masing butuh login client lain lewat langkah ganti akun eksplisit (langkah 7 sampai 9 dan 15 sampai 17). Bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras karena tiap client membawa data dan login sendiri (prinsip 3, pemisah "beda akun, role, atau entity" kasus b); tidak ada kelas harness campuran.
- Pembukaan Global Settings > Hardware > Handheld Reader untuk TC-GS-HHR-15 dilakukan hook `beforeEach`; TC-GS-HHR-16 dan 17 membukanya lewat langkah eksplisit sesudah ganti akun.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 dan 15 (logout), langkah 8 dan 16 (login).
- TC-GS-HHR-17 Expected c diasersi pada langkah 23 sampai 25; langkah 21 dan 22 memetakan Expected b (tidak ada tombol aksi pada empty state, tombol `[+ Activate Reader]` hanya di toolbar).
- Langkah 6 (TC-GS-HHR-15 Expected c) mengasersi komposisi Used berdasar status Seed Reader A; Seed Reader A tidak memuat reader berstatus selain keempat status itu.
- Temuan untuk QA:
  - Email akun Total Control Client Q dan Client E tidak tertulis di Tabel Data Uji Pre-setup TC (hanya pola `totalControl_automated_{namaClient}@qwertysystem.net`); nama env password Client Q dan Client E tidak ditetapkan TC dan disediakan tim FE.
  - TC-GS-HHR-16 dan 17 tidak menyebut cara berpindah antar client; spec memakai logout lalu login akun Total Control client terkait.
