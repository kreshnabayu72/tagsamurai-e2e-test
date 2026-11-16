# Eliminasi Step: Global Settings > Role

Modul: Role  
Sumber: specs/GlobalSettings/Role  
Tanggal: 2026-11-14

## Kriteria

- A. Persona Distributor atau Partner: langkah yang dijalankan saat persona Distributor atau Partner aktif (termasuk login menuju persona itu). Persona Principal tetap dipertahankan.
- B. Halaman detail: (1) halaman detail user di Admin Console > Settings > User List, termasuk tab dan sub-tab di dalamnya; (2) halaman detail client di Admin Console > Client List. Langkah yang membuka, memverifikasi, atau beroperasi di halaman itu dikecualikan, termasuk aksi yang masuk ke halaman itu (klik Name, menu Detail). Tidak termasuk B: detail user di Global Settings > User, detail user di Fixed Asset > Settings > User, Detail Login User yang dibuka dari Global Settings, Detail Non-Login User, Detail Role, Detail Brand, dan detail lain.
- C. Fitur AI (modul Import): langkah yang menguji AI, termasuk setup mock AI yang hanya untuk AI.
- D. Menu Approval: hanya menu Approval di Admin Console (sidebar atau halaman Admin Console > Approvals, termasuk Tab Active dan History) dan langkah yang masuk atau beroperasi di dalamnya. Approval di Fixed Asset (menu, antrean, Submit for Approval, Waiting for Approval, Approve atau Reject lewat UI atau API) tidak dikecualikan. Sub-tab Pending Approvals pada Responsibilities detail user (Global Settings maupun Fixed Asset) tidak dikecualikan. Teks approval di dialog, TAG Log, dan notifikasi bukan D. Tidak ada langkah di modul ini yang masuk atau beroperasi di Admin Console > Approvals, sehingga D tidak dipicu.
- E. Surface mobile atau Android, serta resize viewport desktop. Yang dikecualikan: langkah yang mengubah atau memulihkan ukuran viewport browser desktop, dan langkah verifikasi yang hanya ada karena resize itu (gulir horizontal, kolom beku, layout viewport sempit, walkthrough tertutup saat resize). Langkah campuran (resize bersama aksi lain dalam satu langkah) dipertahankan.
- Catatan modul: Tidak ada persona Distributor atau Partner di modul ini.

## Daftar Eliminasi

| Spek | Judul | Langkah dikecualikan | Kriteria | Alasan | Dependensi |
|---|---|---|---|---|---|
| TC-GS-ROLE-E2E-012-mobile-detail-selection-mode-header-import-data-toggle-dan-pagination | Mobile Detail Role: Header Import data, Keluar dari Selection Mode, Toggle Inert, dan Pagination Card List | 1-58 | E | Seluruh langkah dijalankan di aplikasi Android uji (Mobile Detail Role: header, selection mode, toggle, pagination card list) | Tidak ada |
| TC-GS-ROLE-E2E-013-mobile-detail-long-press-multi-select-dan-bulk-remove | Mobile Detail Role: Long Press Multi-Select, Floating Bottom Bulk Bar, dan Select All | 1-20 | E | Seluruh langkah dijalankan di aplikasi Android uji (Mobile Detail Role: long press, bulk bar, select all) | Tidak ada |
| TC-GS-ROLE-E2E-014-mobile-card-list-tab-bottom-sheet-dan-toolbar | Mobile Card List Role: Tab Total Control, Tab Read Only, Tab System, Toolbar, dan Bottom Sheet | 1-59 | E | Seluruh langkah dijalankan di aplikasi mobile (Mobile Card List Role: tab, toolbar, bottom sheet) | Tidak ada |

## Ragu / Perlu Konfirmasi

Tidak ada.
