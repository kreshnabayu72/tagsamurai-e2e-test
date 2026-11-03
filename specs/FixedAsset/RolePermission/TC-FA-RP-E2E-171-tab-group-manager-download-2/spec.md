---
id: TC-FA-RP-E2E-171-tab-group-manager-download-2
title: "Tab Group Manager: Download (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-572
  - TC-FA-RP-574
  - TC-FA-RP-1004
coverage:
  web: automated
---

# Tab Group Manager: Download (2/2)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #38 (Tab Group Manager enam baris) dan #18 (pohon group). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): membaca berkas unduhan (nama berkas, nama kolom, jumlah dan nama baris).
- State yang diubah: tidak ada (Search dan node Sidebar Group Tree dikembalikan pada langkah penghubung).

## Test Steps

### Extension berkas mengikuti pilihan format (TC-FA-RP-572)

1. Klik Tab `Group Manager`
2. Klik ikon Download lalu `Download as CSV`
3. Verifikasi berkas `Role-Permission-Group-Manager.csv` terunduh untuk pilihan CSV
4. Klik ikon Download lalu `Download as XLSX`
5. Verifikasi berkas `Role-Permission-Group-Manager.xlsx` terunduh untuk pilihan XLSX

### Download dengan nol baris (TC-FA-RP-574)

6. Ketik Search `zzzz`, tekan Enter
7. Verifikasi empty state `No results found` tampil
8. Verifikasi tombol Download tetap aktif
9. Klik ikon Download lalu `Download as CSV`
10. Verifikasi berkas hanya memuat baris header kolom
11. Kosongkan isi kotak search, tekan Enter

### Download mengikuti node Sidebar Group Tree bersama Search aktif (TC-FA-RP-1004)

12. Klik node `Data Center` di Sidebar Group Tree
13. Klik ikon Download lalu `Download as CSV`
14. Verifikasi tidak ada toast sukses
15. Verifikasi berkas `Role-Permission-Group-Manager.csv` terunduh
16. Verifikasi berkas memuat baris penugasan langsung Kevin Susanto di `Data Center`
17. Verifikasi baris Fajar Nugroho, Lina Marlina, Dimas Pranata, dan Kevin Susanto di `Helpdesk` tidak ada pada berkas
18. Ketik Search `kevin`, tekan Enter
19. Klik node `Helpdesk` di Sidebar Group Tree
20. Klik ikon Download lalu `Download as XLSX`
21. Verifikasi tidak ada toast sukses
22. Verifikasi berkas `Role-Permission-Group-Manager.xlsx` terunduh
23. Verifikasi berkas hanya memuat baris Kevin Susanto di `Helpdesk` (Search `kevin` dan node `Helpdesk` aktif bersama)
24. Kosongkan isi kotak search, tekan Enter

## Notes

- Asersi "tidak ada toast sukses" (langkah 14 dan 21) diletakkan segera setelah pemicu dan sebelum asersi artefak; klik format menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh (bagian 8b butir 11).
- Asersi berkas terbatas pada nama berkas, nama kolom, serta jumlah dan nama baris; isi sel tidak diasersi (kelas fungsional, prinsip 13f).
- Langkah 7 (empty state `No results found`) ditambahkan sebagai anchor positif bahwa Search sudah diproses sebelum asersi berkas hanya berisi header (bagian 8b butir 2); bukan dari Expected TC.
- Langkah 17: baris Kevin Susanto di `Data Center` pada langkah 16 menjadi anchor positif bagi asersi absence baris lain pada berkas.
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab (langkah 1); mengosongkan Search (langkah 11 dan 24).
- Temuan untuk QA:
  - TC-FA-RP-574 Expected ("tombol Download tetap aktif") tidak menyebut kapan tombol diamati; spec mengamatinya sebelum mengeklik Download (langkah 8).
  - TC-FA-RP-1004 Expected a dan c ("terunduh tanpa toast sukses") dipecah menjadi dua klausa; absence toast diasersi sebelum berkas terunduh.
  - TC-FA-RP-1004 langkah 1 tidak menyebut bahwa node dipilih tanpa Search aktif; spec mengikuti urutan TC (langkah 12).
