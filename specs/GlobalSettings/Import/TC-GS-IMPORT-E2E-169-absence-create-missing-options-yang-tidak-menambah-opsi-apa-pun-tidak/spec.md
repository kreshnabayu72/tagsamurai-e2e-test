---
id: TC-GS-IMPORT-E2E-169-absence-create-missing-options-yang-tidak-menambah-opsi-apa-pun-tidak
title: "Absence: Create Missing Options yang tidak menambah opsi apa pun tidak menulis entri log"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-923
coverage:
  web: automated
---

# Absence: Create Missing Options yang tidak menambah opsi apa pun tidak menulis entri log

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): draft Client C dibagikan ke seluruh admin dan Changelog Custom Field Client C bersifat permanen sehingga asersi memakai baseline; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client C dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE): skrip fixture reset Client C ke tanpa draft pada Sub-Tab User Login (Kontrak Fixture R1).
- Baseline log (S-12): total entri Changelog Custom Field dicatat dari teks Pagination "Showing [From] - [To] of [N] items" (0 bila yang tampil adalah empty state) sebelum aksi pemicu; asersi memakai selisih terhadap baseline, bukan angka absolut.
- Data Pre-setup Client C (hanya dibaca, tidak diubah spec ini): Custom Field `Shift` (Dropdown) Active dengan opsi `Pagi`, `Siang`, `Malam`; `Lembur` dan `Piket` belum menjadi opsi.
- Data Dinamis (milik spec ini; draft dibuang oleh reset): D-83 `user-login-shift-longname.csv`: header `First Name,Last Name,Email,Division,Position,Access,Shift`; 2 baris: #1 Siti Rahmawati Shift huruf `A` diulang 121 kali; #2 Budi Santoso Shift huruf `B` diulang 121 kali; Division `Engineering`, Position kosong, Access `Global Settings`. Hasil staging: kedua baris `error`.
- Pemulihan (hook `after`): hapus draft User Login Client C dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-923: Create Missing Options yang tidak menambah opsi apa pun tidak menulis entri log

1. Reset Client C ke tanpa draft pada Sub-Tab User Login (aksi fixture)
2. Buka Global Settings > User > Custom Field, lalu klik icon `[Changelog]`
3. Catat angka total pada teks Pagination Changelog Custom Field (Showing [From] - [To] of [N] items; 0 bila yang tampil adalah empty state) sebagai baseline
4. Tutup modal Changelog
5. Buka Global Settings > Import, pilih Sub-Tab User Login
6. Klik `[Upload File]` di Dropzone dan pilih berkas `user-login-shift-longname.csv`
7. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
8. Klik `[Create Missing Options]` pada baris pesan "Shift: Invalid option" di Error Summary Callout
9. Verifikasi toast error: "Error, failed to create option."
10. Buka Global Settings > User > Custom Field, lalu klik icon `[Changelog]`
11. Verifikasi modal Changelog Custom Field terbuka
12. Verifikasi angka total Pagination Changelog Custom Field sama dengan baseline langkah 3 (tidak ada entri baru)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: asersi absence (g) dengan aksi nyata di spec ini (upload, Confirm Mapping, Create Missing Options) dan baseline sendiri, sehingga memenuhi S-05.
- Spec singkat (12 langkah) sehingga tidak melewati sekitar 35 langkah.
- Langkah penghubung (tanpa `Verifikasi`): reset (langkah 1), pembukaan halaman dan Sub-Tab, pencatatan baseline (langkah 3), dan menutup modal Changelog (langkah 4). Langkah 9 (toast error) menjadi anchor positif yang terhubung ke pemicu sebelum asersi absence entri pada langkah 12. Langkah 11 (modal Changelog Custom Field terbuka) menjadi anchor positif pada surface yang sama sebelum asersi absence (D-15, K-5); surface yang diperiksa hanya Changelog Custom Field karena itu satu-satunya surface yang disebut TC.
- Pembagian TC lintas spec: TC-GS-IMPORT-923 hanya ada di spec ini; Create Missing Options yang sukses (menambah opsi) dan pencatatan entri log Custom Field ada di spec lain (S4 dan S6).
- Temuan untuk QA:
  - TC-GS-IMPORT-923 tidak menyebut anchor modal Changelog sebelum asersi absence entri; langkah 11 menambahkan `Verifikasi` modal Changelog Custom Field terbuka sebagai anchor positif (baseline boleh 0).
  - TC-GS-IMPORT-923 mengasersi absence entri log hanya di Changelog Custom Field dan tidak menyebut System Log atau Activity Log; spec hanya memeriksa surface yang disebut TC (butir 2 bagian 8b: surface disebut satu per satu).
  - TC-GS-IMPORT-923 Expected a menyebut toast error "Error, failed to create option." sebagai akibat dua nama 121 karakter; penyebab kegagalan (nama melebihi 120 karakter) tidak dijelaskan di Expected.
  - Post Condition TC-GS-IMPORT-923 ("draft berisi 2 baris `error`; tidak ada opsi baru") tidak punya langkah observasi di TC dan tidak diasersi (S-01).
