# Eliminasi Step: Global Settings > Brand

Modul: Brand, Sumber: specs/GlobalSettings/Brand, Tanggal 2026-11-14

## Kriteria

- **A. Persona Distributor atau Partner:** persona aktif dilacak dari Prerequisites dan langkah login, logout, ganti akun, atau ganti company. Langkah yang dijalankan saat persona Distributor atau Partner aktif dikecualikan, termasuk login menuju persona itu. Akun Client (Total Control Client A, B, C, dan seterusnya) bukan Distributor atau Partner, sehingga tidak dikecualikan. Langkah saat persona Principal dipertahankan.
- **B. Halaman detail:** hanya (1) halaman detail user di Admin Console > Settings > User List, termasuk tab dan sub-tab di dalamnya, dan (2) halaman detail client di Admin Console > Client List. Langkah yang membuka, memverifikasi, atau beroperasi di halaman itu dikecualikan, termasuk aksi yang masuk ke halaman itu (klik Name, menu Detail). Detail user di Global Settings > User, detail user di Fixed Asset > Settings > User, Detail Non-Login User, Detail Role, Detail Brand, dan detail lain tidak termasuk.
- **C. Fitur AI:** tidak ditemukan pada modul ini.
- **D. Menu Approval:** hanya menu Approval di Admin Console (sidebar atau halaman Admin Console > Approvals, termasuk Tab Active dan History) dan langkah yang masuk atau beroperasi di dalamnya. Approval di Fixed Asset (menu, antrean, Submit for Approval, Waiting for Approval, Approve atau Reject lewat UI atau API) tidak dikecualikan. Sub-tab Pending Approvals pada Responsibilities detail user (Global Settings maupun Fixed Asset) tidak dikecualikan. Teks approval di dialog, TAG Log, dan notifikasi bukan D. Tidak ada langkah di modul ini yang masuk atau beroperasi di Admin Console > Approvals, sehingga D tidak dipicu.
- **E. Surface mobile atau Android, serta resize viewport desktop:** langkah yang menguji layout mobile, aplikasi Android, atau bottom sheet mobile. Langkah yang mengubah atau memulihkan ukuran viewport browser desktop (persempit, perkecil, atur lebar, kembalikan atau pulihkan viewport) dikecualikan dengan alasan resize viewport desktop. Langkah campuran (resize bersama aksi lain dalam satu langkah) dipertahankan dan dicatat di Ragu. Termasuk langkah verifikasi yang hanya ada karena resize itu (gulir horizontal, kolom beku, layout viewport sempit, walkthrough tertutup saat resize).
- Langkah login, buka list, dan search yang mendahului halaman detail dipertahankan.

Ringkasan: 6 spek punya eliminasi; 46 dari 2326 langkah bernomor dikecualikan. Langkah yang dikecualikan sebagian (misalnya iterasi persona) dinyatakan di kolom Langkah dikecualikan.

## Daftar Eliminasi

| Spek | Judul | Langkah dikecualikan | Kriteria | Alasan | Dependensi |
|---|---|---|---|---|---|
| TC-GS-BRAND-E2E-001 | Screening Tab Brand: Layout, Tab Default, Tooltip Table Tools, dan Layout Tablet | 29, 32, 34-35 (E) | E | resize viewport desktop (langkah 29, 35); verifikasi setelah resize viewport desktop (langkah 32, 34) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-BRAND-E2E-008 | Flag Seen dan Dismiss Guided Tooltip Tab Brand | 17-21 (E) | E | resize viewport desktop (langkah 17, 21); verifikasi setelah resize viewport desktop (langkah 18-20) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-BRAND-E2E-041 | Setup Column Tabel Brand: Reorder, Pin, dan Reset to Default | 10, 14-15, 17-18 (E) | E | resize viewport desktop (langkah 10, 18); verifikasi setelah resize viewport desktop (langkah 14-15, 17) | Tidak ada ketergantungan yang terdeteksi. |
| TC-GS-BRAND-E2E-044 | Used By (Items) Sama dengan Total Item di Detail pada Instance Principal dan Distributor | 8-13 (A) | A | Login ke persona Total Control Distributor (langkah 8) dan langkah yang dijalankan saat persona itu aktif (9-13) | Tidak ada. Langkah 7 (logout dari Principal, dipertahankan) menjadi titik keluar persona; spec berakhir pada persona Distributor. |
| TC-GS-BRAND-E2E-057 | Brand Detail: Device SKU List pada Instance Principal dan Distributor | 35-43 (A) | A | Login ke persona Total Control Distributor (langkah 35) dan langkah yang dijalankan saat persona itu aktif (36-43) | Langkah 34 (logout dari Principal, dipertahankan) menjadi titik keluar persona; tidak ada langkah dipertahankan setelah 35. |
| TC-GS-BRAND-E2E-074 | Mobile Android: Card List Brand dan Selection Mode untuk Bulk Delete | 1-25 (E) | E | Menguji surface mobile atau Android | Tidak ada ketergantungan yang terdeteksi. |

## Ragu / Perlu Konfirmasi

Tidak ada.
