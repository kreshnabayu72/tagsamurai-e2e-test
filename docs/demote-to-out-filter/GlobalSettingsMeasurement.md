# Eliminasi Step: Global Settings > Measurement

Modul: Measurement  
Sumber: specs/GlobalSettings/Measurement  
Tanggal: 2026-11-14

## Kriteria

- A. Persona Distributor atau Partner: langkah yang dijalankan saat persona Distributor atau Partner aktif (termasuk login menuju persona itu). Persona Principal tetap dipertahankan.
- B. Halaman detail: (1) halaman detail user di Admin Console > Settings > User List, termasuk tab dan sub-tab di dalamnya; (2) halaman detail client di Admin Console > Client List. Langkah yang membuka, memverifikasi, atau beroperasi di halaman itu dikecualikan, termasuk aksi yang masuk ke halaman itu (klik Name, menu Detail). Tidak termasuk B: detail user di Global Settings > User, detail user di Fixed Asset > Settings > User, Detail Login User yang dibuka dari Global Settings, Detail Non-Login User, Detail Role, Detail Brand, dan detail lain.
- C. Fitur AI (modul Import): langkah yang menguji AI, termasuk setup mock AI yang hanya untuk AI.
- D. Menu Approval: hanya menu Approval di Admin Console (sidebar atau halaman Admin Console > Approvals, termasuk Tab Active dan History) dan langkah yang masuk atau beroperasi di dalamnya. Approval di Fixed Asset (menu, antrean, Submit for Approval, Waiting for Approval, Approve atau Reject lewat UI atau API) tidak dikecualikan. Sub-tab Pending Approvals pada Responsibilities detail user (Global Settings maupun Fixed Asset) tidak dikecualikan. Teks approval di dialog, TAG Log, dan notifikasi bukan D. Tidak ada langkah di modul ini yang masuk atau beroperasi di Admin Console > Approvals, sehingga D tidak dipicu.
- E. Surface mobile atau Android, serta resize viewport desktop. Yang dikecualikan: langkah yang mengubah atau memulihkan ukuran viewport browser desktop, dan langkah verifikasi yang hanya ada karena resize itu (gulir horizontal, kolom beku, layout viewport sempit, walkthrough tertutup saat resize). Langkah campuran (resize bersama aksi lain dalam satu langkah) dipertahankan.
- Catatan modul: Persona Distributor muncul di 004, 029, dan 055.

## Daftar Eliminasi

| Spek | Judul | Langkah dikecualikan | Kriteria | Alasan | Dependensi |
|---|---|---|---|---|---|
| TC-GS-UOM-E2E-001-screening-tab-measurement-layout-tooltip-dan-sticky | Screening Tab Measurement: Layout, Tab Default, Tooltip Table Tools, Sticky Kolom, Katalog Flat | 30, 32-38 (E) | E | resize viewport desktop (langkah 30, 38); verifikasi setelah resize viewport desktop (langkah 32-37) | Tidak ada |
| TC-GS-UOM-E2E-004-used-by-items-sama-dengan-total-item-per-instance | Used By (Items) = Total Item pada Instance Client, Principal, dan Distributor | 19-27 | A | Login ke persona Distributor (langkah 19) dan seluruh verifikasi pada instance Distributor (20-27) | Tidak ada |
| TC-GS-UOM-E2E-011-guided-tooltip-flag-seen-dan-dismiss | Flag Seen dan Dismiss Guided Tooltip: Skip, Overlay, Tombol [?], Resize, Navigasi Halaman | 32-36 (E) | E | resize viewport desktop (langkah 32, 36); verifikasi setelah resize viewport desktop (langkah 33-35) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-UOM-E2E-029-delete-blokir-in-use-client-dan-principal | Delete Unit Diblokir karena In-Use: FAMS, SAMS, Admin Console Principal dan Distributor, dan Breakdown | 28-35 | A | Login ke persona Distributor (langkah 28) dan seluruh langkah pada instance Distributor (29-35) | Tidak ada |
| TC-GS-UOM-E2E-043-setup-column-tabel-reorder-pin-dan-reset | Setup Column Tabel Measurement: Reorder (Modal dan Panel), Pin, dan Reset to Default | 27, 32-33, 37-38, 43-44, 48-50 (E) | E | resize viewport desktop (langkah 27, 50); verifikasi setelah resize viewport desktop (langkah 32-33, 37-38, 43-44, 48-49) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-UOM-E2E-052-changelog-setup-column-reorder-pin-dan-reset | Changelog Measurement: Setup Column Reorder (Modal dan Panel), Pin Maksimal 3, dan Reset to Default | 22, 26-27, 31-32, 41-43 (E) | E | resize viewport desktop (langkah 22, 43); verifikasi setelah resize viewport desktop (langkah 26-27, 31-32, 41-42) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-UOM-E2E-055-detail-device-name-list-principal-dan-distributor | Unit Detail: Device Name List pada Principal dan Distributor (Screening, Search, Sort, Empty State) | 6-8 | B | Membuka Detail Andi Pratama di Admin Console > Settings > User (langkah 6) dan memverifikasi Avatar Header Detail user di Admin Console (7-8); langkah 3-5 (buka list dan search) tetap dipertahankan | Tidak ada |
| TC-GS-UOM-E2E-056-detail-setup-column-item-type-list | Unit Detail: Setup Column Item Type List (Screening, Hide, Reorder, Pin, Reset, Tutup, Guard) | 65, 69-70, 74-76 (E) | E | resize viewport desktop (langkah 65, 76); verifikasi setelah resize viewport desktop (langkah 69-70, 74-75) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-UOM-E2E-057-detail-setup-column-device-name-list | Unit Detail Principal: Setup Column Device Name List | 26, 30-31, 35-37 (E) | E | resize viewport desktop (langkah 26, 37); verifikasi setelah resize viewport desktop (langkah 30-31, 35-36) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-UOM-E2E-074-mobile-card-list-menu-dan-dialog | Mobile Android: Card List, Tap Detail, Menu Card, Search, Filter, Create, dan Delete sebagai Bottom Sheet | 1-43 | E | Seluruh langkah dijalankan di aplikasi mobile Android (card list, bottom sheet, tap, long-press) | Tidak ada |
| TC-GS-UOM-E2E-075-mobile-selection-mode-bulk-delete | Mobile Android: Selection Mode Bulk Delete (Long-Press, Cancel, Commit, Tanpa Capability Delete) | 1-28 | E | Seluruh langkah dijalankan di aplikasi mobile Android (selection mode, long-press, tap card) | Tidak ada |

## Ragu / Perlu Konfirmasi

Tidak ada.
