# Eliminasi Step: Fixed Asset > SettingsUser

Modul: SettingsUser
Sumber: specs/FixedAsset/SettingsUser
Tanggal: 2026-11-14

## Kriteria

- **A. Persona Distributor atau Partner**: tidak dipicu. Akun login di seluruh spek modul ini adalah akun Total Control atau akun role pada company Principal (pola `totalControl_*`, `readOnly_*`, `groupManager_*`, dst.). Tidak ditemukan spek yang login, logout, atau ganti akun ke akun Distributor atau Partner.
- **B. Halaman detail**: hanya mencakup (1) halaman detail user di Admin Console > Settings > User List, termasuk tab dan sub-tab di dalamnya, dan (2) halaman detail client di Admin Console > Client List. Modul ini adalah Fixed Asset > Settings > User, sehingga Detail User di sini bukan halaman B dan seluruh langkahnya dipertahankan kecuali kena kriteria lain. Spek modul ini tidak menyentuh Admin Console, jadi B tidak dipicu sama sekali. Langkah login, buka list, search, dan buka Detail User Fixed Asset tetap dipertahankan.
- **C. Fitur AI**: tidak ada. Pencarian `AI`, `chatbot`, `OCR`, dan `asisten` di seluruh spek Fixed Asset tidak menemukan fitur AI.
- **D. Menu Approval**: hanya menu Approval di Admin Console (sidebar atau halaman Admin Console > Approvals, termasuk Tab Active dan History) dan langkah yang masuk atau beroperasi di dalamnya. Approval di Fixed Asset (menu, antrean, Submit for Approval, Waiting for Approval, Approve atau Reject lewat UI atau API) tidak dikecualikan. Sub-tab Pending Approvals pada Responsibilities detail user (Global Settings maupun Fixed Asset) tidak dikecualikan. Teks approval di dialog, TAG Log, dan notifikasi bukan D. Tidak ada langkah di modul ini yang masuk atau beroperasi di Admin Console > Approvals, sehingga D tidak dipicu.
- **E. Surface mobile atau Android, serta resize viewport desktop**: langkah yang menguji aplikasi Android, aplikasi mobile, bottom sheet, card list, atau long press dikecualikan. Semua langkah UI di spek berjudul `android` atau `mobile` dikecualikan, sedangkan langkah seed atau fixture API di spek tersebut dipertahankan. Penyebutan Android, Mobile App, atau Mobile sebagai nilai data tidak dikecualikan. Langkah yang mengubah atau memulihkan ukuran viewport browser desktop (persempit, perkecil, atur lebar, kembalikan atau pulihkan viewport) dikecualikan dengan alasan resize viewport desktop. Langkah campuran (resize bersama aksi lain dalam satu langkah) dipertahankan dan dicatat di Ragu. Termasuk langkah verifikasi yang hanya ada karena resize itu (gulir horizontal, kolom beku, layout viewport sempit, walkthrough tertutup saat resize).

Catatan metode: himpunan langkah dikecualikan dihitung ulang dari spek sebagai A, B, C, D, E (D hanya menu Approval di Admin Console; E termasuk resize viewport desktop). Klasifikasi memakai aturan teks (pencarian) dan pemeriksaan langkah yang menyebut Admin Console > Approvals serta langkah resize viewport. Ini bukan pembacaan manual setiap langkah, sehingga perlu verifikasi sampling sebelum eliminasi dijalankan.

Ringkasan: 3 spek punya eliminasi, 104 dari 15635 langkah bernomor dikecualikan, 0 item di Ragu.

## Daftar Eliminasi

| Spek | Judul | Langkah dikecualikan | Kriteria | Alasan | Dependensi |
|---|---|---|---|---|---|
| TC-FA-SU-E2E-006-guided-tooltip-user-list-kunjungan-pertama-navigasi-replay-dan-exit | Guided Tooltip User List: Kunjungan Pertama, Navigasi, Replay, dan Exit | 40-44, 52 | E | resize viewport desktop (langkah 40, 52); verifikasi setelah resize viewport desktop (langkah 41-44) | - |
| TC-FA-SU-E2E-013-android-kartu-user-list-row-action-toolbar-seleksi-dan-drawer-group-tree | Android: Kartu User List, Row Action, Toolbar, Seleksi, dan Drawer Group Tree | 1-33 | E | surface mobile/Android (spec mobile/Android) | - |
| TC-FA-SU-E2E-014-android-detail-user-card-list-modal-tooltip-disabled-countdown-resend-dan-bottom-sheet | Android: Detail User, Card List, Modal, Tooltip Disabled, Countdown Resend, dan Bottom Sheet | 1-69 | E | surface mobile/Android (spec mobile/Android) | - |

## Ragu / Perlu Konfirmasi

Tidak ada.
