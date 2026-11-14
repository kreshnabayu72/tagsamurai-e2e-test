# Eliminasi Step: Global Settings > Position

Modul: Position  
Sumber: specs/GlobalSettings/Position  
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
| TC-GS-POS-E2E-005-guided-tooltip-konten-navigasi-keyboard | Guided Tooltip Tab Position: Konten Step, Navigasi Next/Back, Resize Viewport, Keyboard, dan Identik untuk Read Only | 39-45 (E) | E | resize viewport desktop (langkah 39, 41); verifikasi setelah resize viewport desktop (langkah 40, 42-45) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-POS-E2E-027-mobile-selection-mode-dan-bulk-delete | Mobile Android: Aturan Card dan Menu, Screening Toolbar, dan Selection Mode Long-press untuk Bulk Delete Position | 1-39 | E | Seluruh langkah dijalankan di aplikasi Android (Mobile Android: card, selection mode, long-press, bottom sheet) | Tidak ada |
| TC-GS-POS-E2E-032-setup-column-modal-tabel-utama | Popup Setup Column Tabel Position: Screening, Footer, Search, Hide, Reorder, Pin, Reset, Penutupan, dan Independensi dari Popup Changelog | 82, 87-88, 90-91, 96-97, 103 (E) | E | resize viewport desktop (langkah 82, 103); verifikasi setelah resize viewport desktop (langkah 87-88, 90-91, 96-97) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-POS-E2E-042-changelog-column-visibility-dan-setup-column | Popup Changelog: Overlay Column Visibility dan Setup Column 7 Kolom (Hide, Reorder, Pin, Reset to Default, ✕, dan Kolom Terakhir) | 145, 151-154, 162 (E) | E | resize viewport desktop (langkah 145, 162); verifikasi setelah resize viewport desktop (langkah 151-154) | Tidak ada ketergantungan yang terdeteksi. |

## Ragu / Perlu Konfirmasi

Tidak ada.
