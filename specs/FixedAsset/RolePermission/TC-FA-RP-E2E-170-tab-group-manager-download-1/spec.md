---
id: TC-FA-RP-E2E-170-tab-group-manager-download-1
title: "Tab Group Manager: Download (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-567
  - TC-FA-RP-568
  - TC-FA-RP-569
  - TC-FA-RP-570
coverage:
  web: automated
---

# Tab Group Manager: Download (1/2)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #38 (Tab Group Manager enam baris) dan #18 (pohon group). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): membaca berkas unduhan (nama berkas, nama kolom, jumlah dan nama baris).
- State yang diubah: konfigurasi kolom Setup Column Tab Group Manager (kolom Division disembunyikan lalu ditampilkan); hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).

## Test Steps

### Tanpa Search atau Filter mengekspor seluruh data (TC-FA-RP-567)

1. Klik Tab `Group Manager`
2. Klik ikon Download lalu `Download as CSV`
3. Verifikasi tidak ada toast sukses
4. Verifikasi berkas `Role-Permission-Group-Manager.csv` terunduh
5. Verifikasi berkas memuat kolom Name, Group, Position, Division, Status, Modified By, Last Updated
6. Verifikasi berkas memuat seluruh enam baris Pre-setup #38

### Search dan Filter aktif hanya mengekspor baris yang cocok (TC-FA-RP-568)

7. Ketik Search `kevin`, tekan Enter
8. Klik ikon Filter, pilih opsi `IT Operations` pada field Division, klik `[Apply]`
9. Klik ikon Download lalu `Download as XLSX`
10. Verifikasi berkas `Role-Permission-Group-Manager.xlsx` terunduh
11. Verifikasi berkas hanya memuat dua baris Kevin Susanto (`Data Center` dan `Helpdesk`)
12. Kosongkan isi kotak search, tekan Enter
13. Klik ikon Filter, klik `[Clear Field]` lalu `[Apply]`

### Kolom yang disembunyikan tidak ikut diekspor (TC-FA-RP-569)

14. Klik header `(⋯)` kolom Column Visibility, klik `Setup Column...`, hapus centang kolom `Division`, lalu klik `[Save]`
15. Klik ikon Download lalu `Download as CSV`
16. Verifikasi berkas tidak memuat kolom `Division`
17. Verifikasi kolom berkas sama dengan kolom yang sedang tampil: Name, Group, Position, Status, Modified By, Last Updated

### Kolom yang ditampilkan kembali ikut diekspor (TC-FA-RP-570)

18. Klik header `(⋯)` kolom Column Visibility, klik `Setup Column...`, centang kembali kolom `Division`, lalu klik `[Save]`
19. Klik ikon Download lalu `Download as CSV`
20. Verifikasi berkas memuat kembali kolom `Division`

## Notes

- Asersi "tidak ada toast sukses" (langkah 3) diletakkan segera setelah pemicu dan sebelum asersi artefak; klik format menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh (bagian 8b butir 11).
- Asersi berkas terbatas pada nama berkas, nama kolom, serta jumlah dan nama baris; isi sel tidak diasersi (kelas fungsional, prinsip 13f).
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab (langkah 1); membersihkan Search dan Filter (langkah 12 dan 13); membuka Setup Column dan menyimpan (langkah 14 dan 18).
- TC-FA-RP-570 bergantung pada TC-FA-RP-569; kolom `Division` sudah tersembunyi pada langkah 14 sehingga langkah "sembunyikan lalu tampilkan" TC-FA-RP-570 dilebur menjadi langkah 18 yang hanya menampilkannya kembali.
- Temuan untuk QA:
  - TC-FA-RP-568 Expected b menyebut dua baris Kevin Susanto, yang identik pada Name, Position, dan Division; spec membedakannya lewat kolom Group.
  - TC-FA-RP-569 Expected ("file sama dengan kolom yang sedang tampil") diasersi sebagai klausa terpisah pada langkah 17.
