---
id: TC-GS-UCF-E2E-014-isolasi-entitas
title: "Isolasi Entitas: Custom Field dan Changelog Client A Tidak Terlihat di Client B, dan Field Name yang Sama dengan Client A Diterima di Client B"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UCF-307
  - TC-GS-UCF-421
coverage:
  web: automated
---

# Isolasi Entitas: Custom Field dan Changelog Client A Tidak Terlihat di Client B, dan Field Name yang Sama dengan Client A Diterima di Client B

## Prerequisites

- Mode: FE+BE (backend nyata).
- Kelas c (multi-konteks, dua client): dua entitas (Client A dan Client B) dalam satu spec, tetapi sesi UI hanya satu (Client B); Client A hanya menjadi sumber data Pre-setup yang tidak boleh terlihat dan tidak ada sesi UI Client A.
- Akun aktor: Total Control Client B (Lina Kusuma, Modified By `Lina K`) `totalControl_automated_qaTeam2@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTB_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun Total Control default suite (`Spectra.env.GS_TC_PASSWORD`).
- Layar awal: hook `beforeEach` suite membuka Global Settings > User > Custom Field untuk akun Client B; spec ini tidak menguji navigasi sehingga tidak mengulang langkah buka.
- Data Pre-setup (tetap di environment, hanya dibaca): Client A memiliki Custom Field `Cost Center` (precondition TC-GS-UCF-307) dan `Employee Grade` (precondition TC-GS-UCF-421), keduanya Pre-setup Client A; Client B memiliki `Client B Field` (D-85: Text, Active, Required No, dibuat Lina Kusuma) dan 9 field Pre-setup lain (10 Pre-setup; `Client B Eleven` D-87 bukan Pre-setup dan tidak dipakai spec ini) serta tidak memiliki field bernama `Employee Grade`. Tidak bersuffix karena Pre-setup.
- Data Dinamis: tidak ada yang di-seed. TC-GS-UCF-421 membuat `Employee Grade` di Client B lewat UI dan menghapusnya di akhir TC yang sama. Nama `Employee Grade` ditulis literal tanpa suffix karena objek uji adalah kesamaan nama persis dengan field Pre-setup Client A (pengecualian S-12 butir (ii)): seeding idempotent (tidak ada seeding; field dibuat TC), hook `before` memastikan Client B tidak memiliki field bernama `Employee Grade` (menghapus lewat API bila ada sisa dari run sebelumnya), hook `after` menghapus `Employee Grade` Client B bila masih ada, dan suite berjalan serial.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API field `Employee Grade` di Client B bila masih ada; kosongkan Search tabel dan Search Changelog; kembalikan sesi ke akun default suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-custom-field-user` true untuk akun Client B dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pembacaan keberadaan field di entitas Client A dan Client B (disediakan tim FE/BE; mekanisme tidak didefinisikan di TC, PRD, atau LLD); menunggu ±500 ms (debounce pengecekan keunikan Field Name); pembacaan teks Illustration.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`) dan Changelog Client B (entri Create dan Delete `Employee Grade` dari TC-GS-UCF-421 bersifat kumulatif dan tidak memuat `Cost Center`, sehingga tidak memengaruhi Expected d TC-GS-UCF-307). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-UCF-307: Isolasi data antar client, tabel dan Changelog Client B tidak memuat data Client A

1. Ketik Search `Client B Field`, tekan Enter
2. Verifikasi baris `Client B Field` tampil
3. Ganti isi kotak search dengan `Cost Center`, tekan Enter
4. Verifikasi Illustration dengan Title `No results found`
5. Verifikasi Illustration dengan Description `Try adjusting your search or filter.`
6. Klik icon Changelog
7. Ketik Search `Client B Field` pada Changelog, tekan Enter
8. Verifikasi Changelog memuat entri `Client B Field` dengan Modified By `Lina K`
9. Ganti isi kotak search Changelog dengan `Cost Center`, tekan Enter
10. Verifikasi Illustration dengan Title `No results found` pada Changelog
11. Verifikasi Illustration dengan Description `Try adjusting your search or filter.` pada Changelog
12. Tutup popup Changelog dengan `✕`
13. Klik `(←)` pada kotak Search tabel

### TC-GS-UCF-421: Field Name yang sama dengan field Client A diterima di Client B

14. Klik `[+ Custom Field]`
15. Isi Field Name `Employee Grade`, pilih Data Type `Text`, tunggu sekitar 500 ms
16. Verifikasi pesan `Field name already exists` tidak muncul
17. Klik `[Submit]`
18. Verifikasi toast sukses: "Success, custom field has been created."
19. Ketik Search `Employee Grade`, tekan Enter
20. Verifikasi baris `Employee Grade` tampil
21. Verifikasi Modified By baris `Employee Grade` `Lina K`
22. Klik `⋯` pada baris `Employee Grade`, pilih `Delete`, klik `[Delete]` pada dialog
23. Verifikasi toast sukses: "Success, custom field has been deleted."
24. Verifikasi baris `Employee Grade` hilang dari tabel Client B
25. Klik `(←)` pada kotak Search tabel

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Kelas c (multi-konteks, dua client); satu sesi UI (Client B), tanpa harness lain.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC di spec: 307 (baca), lalu 421 (membuat dan menghapus data), sesuai urutan sumber dan bagian 3 prinsip 3. TC-GS-UCF-421 memakai `Employee Grade`, bukan `Cost Center`, sehingga entri Changelog Client B yang kumulatif dari 421 tidak memuat `Cost Center` dan Expected d TC-GS-UCF-307 tetap berlaku pada run berikutnya.
- Langkah 1 TC-GS-UCF-307 ("Buka tab Custom Field") dipenuhi hook `beforeEach` (layar awal), sehingga tidak ada langkah buka di `## Test Steps`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 12 dan 13 (menutup popup Changelog dan mengosongkan Search tabel), langkah 19 (Search untuk menemukan baris `Employee Grade` Client B), dan langkah 25 (mengosongkan Search). Langkah 22 menjalankan Delete sebagai bagian TC-GS-UCF-421 (langkah 5 TC) pada field yang dibuat langkah 17.
- Asersi `No results found` pada langkah 4, 5, 10, dan 11 adalah anchor positif hasil Search (bagian 8b butir 2). Langkah 24 (baris hilang sesudah Delete) beranchor toast sukses langkah 23. Langkah 16 (pesan tidak muncul) beranchor jeda 500 ms sesudah Field Name dan Data Type terisi pada langkah 15.
- Spec ini bukan spec absence (kelas g): Changelog Client B yang tidak memuat `Cost Center` pada TC-GS-UCF-307 adalah asersi isolasi (scope exclusion dengan anchor positif entri `Client B Field`), sedangkan entri Changelog hasil Delete tidak diasersi.
- Temuan untuk QA:
  - TC-GS-UCF-307 langkah 1 tidak menyebut cara membuka tab sebagai Client B; hook `beforeEach` membuka layar awal.
  - TC-GS-UCF-421 langkah 2 menyebut "tunggu sekitar 500 ms" tanpa menyebut asersi saat menunggu; spec mengasersi pesan `Field name already exists` tidak muncul setelah jeda itu (Expected a).
  - TC-GS-UCF-421 Post Condition ("Employee Grade Client B terhapus; field Client B kembali seperti sebelum TC") tidak punya langkah observasi selain Expected d; tidak diasersi di luar toast dan baris hilang.
