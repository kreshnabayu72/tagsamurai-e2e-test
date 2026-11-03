---
id: TC-FA-RP-E2E-172-tab-group-manager-sidebar-group-tree-dan-menu-baris
title: "Tab Group Manager: Sidebar Group Tree dan menu baris"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-575
  - TC-FA-RP-576
coverage:
  web: automated
---

# Tab Group Manager: Sidebar Group Tree dan menu baris

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #38 (Tab Group Manager enam baris) dan #18 (pohon group). Spec tidak mengubah data; menu baris dibuka lalu ditutup tanpa menjalankan Remove. Di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- State yang diubah: tidak ada (Search dikosongkan pada langkah penghubung).

## Test Steps

### Sidebar Group Tree bersama Search (TC-FA-RP-575)

1. Klik Tab `Group Manager`
2. Klik node `Data Center` di Sidebar Group Tree
3. Verifikasi hanya baris Kevin Susanto di `Data Center` yang tampil
4. Ketik Search `kevin`, tekan Enter
5. Klik node `Helpdesk` di Sidebar Group Tree
6. Verifikasi Search `kevin` tetap aktif
7. Verifikasi hanya baris Kevin Susanto di `Helpdesk` yang tampil
8. Kosongkan isi kotak search, tekan Enter

### Menu baris hanya memuat Remove (TC-FA-RP-576)

9. Klik node `IT Infrastructure` di Sidebar Group Tree
10. Klik `[⋯]` pada baris Fajar Nugroho
11. Verifikasi menu memuat `Remove` saja (ikon DeleteBin6Line, severity danger)
12. Tutup menu dengan Esc

## Notes

- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab (langkah 1); mengosongkan Search (langkah 8); langkah 9 memilih node `IT Infrastructure` agar baris Fajar Nugroho (penugasan langsung di node itu) tampil karena node sebelumnya (`Helpdesk`) hanya menampilkan baris Kevin Susanto; menutup menu dengan Esc (langkah 12).
- Asersi "hanya baris X" menyebut nama baris yang tampil sehingga baris itu sendiri menjadi anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-RP-576 langkah 2 tidak menyebut node Sidebar Group Tree yang aktif; baris Fajar Nugroho hanya tampil bila node `IT Infrastructure` dipilih atau tidak ada node terpilih. Spec memilih node `IT Infrastructure` (langkah 9).
  - TC-FA-RP-575 Expected a ("hanya baris Kevin Susanto di `Data Center`") menyiratkan node menampilkan penugasan langsung node itu saja; spec mengikuti Expected TC.
