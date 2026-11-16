# Eliminasi Step: Fixed Asset > SettingsCustomFields

Modul: SettingsCustomFields
Sumber: specs/FixedAsset/SettingsCustomFields
Tanggal: 2026-11-14

## Kriteria

- **A. Persona Distributor atau Partner**: tidak dipicu. Akun login di seluruh spek modul ini adalah akun Total Control atau akun role pada company Principal (pola `totalControl_*`, `readOnly_*`, `groupManager_*`, dst.). Tidak ditemukan spek yang login, logout, atau ganti akun ke akun Distributor atau Partner. Kata Distributor atau Partner yang muncul hanya sebagai nama data (Plan Owner) dicatat di Ragu. Asumsi persona Principal untuk semua langkah lain perlu dikonfirmasi (lihat Ragu).
- **B. Halaman detail**: hanya mencakup halaman detail user di Admin Console > Settings > User List (termasuk tab dan sub-tab di dalamnya) dan halaman detail client di Admin Console > Client List, termasuk aksi yang masuk ke halaman itu (klik Name, menu Detail). Detail user di Fixed Asset > Settings > User, detail user di Global Settings > User, detail aset, dan detail lain di Fixed Asset (Role, Asset Name, Group, Class, mode Edit) bukan B dan dipertahankan. Tidak ditemukan langkah di spek modul ini yang membuka atau beroperasi di halaman detail user atau client Admin Console (langkah yang menyebut Admin Console hanya menyangkut Role & Permission, Activity Log, Plans & Licensing, atau aksi lewat sesi API atau fixture), sehingga B tidak dipicu.
- **C. Fitur AI**: tidak ada. Pencarian `AI`, `chatbot`, `OCR`, dan `asisten` di seluruh spek Fixed Asset tidak menemukan fitur AI.
- **D. Menu Approval**: hanya menu Approval di Admin Console (sidebar atau halaman Admin Console > Approvals, termasuk Tab Active dan History) dan langkah yang masuk atau beroperasi di dalamnya. Approval di Fixed Asset (menu, antrean, Submit for Approval, Waiting for Approval, Approve atau Reject lewat UI atau API) tidak dikecualikan. Sub-tab Pending Approvals pada Responsibilities detail user (Global Settings maupun Fixed Asset) tidak dikecualikan. Teks approval di dialog, TAG Log, dan notifikasi bukan D. Tidak ada langkah di modul ini yang masuk atau beroperasi di Admin Console > Approvals, sehingga D tidak dipicu.
- **E. Surface mobile atau Android, serta resize viewport desktop**: langkah yang menguji aplikasi Android, aplikasi mobile, bottom sheet, card list, atau long press dikecualikan. Semua langkah UI di spek berjudul `android` atau `mobile` dikecualikan, sedangkan langkah seed atau fixture API di spek tersebut dipertahankan. Penyebutan Android, Mobile App, atau Mobile sebagai nilai data (Device atau Browser, nama asset class) tidak dikecualikan. Langkah yang mengubah atau memulihkan ukuran viewport browser desktop (persempit, perkecil, atur lebar, kembalikan atau pulihkan viewport) dikecualikan dengan alasan resize viewport desktop. Langkah campuran (resize bersama aksi lain dalam satu langkah) dipertahankan dan dicatat di Ragu. Termasuk langkah verifikasi yang hanya ada karena resize itu (gulir horizontal, kolom beku, layout viewport sempit, walkthrough tertutup saat resize).

Catatan metode: himpunan langkah dikecualikan dihitung ulang dari spek sebagai A, B, C, D, E (D hanya menu Approval di Admin Console; E termasuk resize viewport desktop). Klasifikasi memakai aturan teks (pencarian) dan pemeriksaan langkah yang menyebut Admin Console > Approvals serta langkah resize viewport. Ini bukan pembacaan manual setiap langkah, sehingga perlu verifikasi sampling sebelum eliminasi dijalankan.

Ringkasan: 4 spek punya eliminasi, 41 dari 5240 langkah bernomor dikecualikan, 0 item di Ragu.

## Daftar Eliminasi

| Spek | Judul | Langkah dikecualikan | Kriteria | Alasan | Dependensi |
|---|---|---|---|---|---|
| TC-FA-CF-E2E-004-truncation-badge-klik-baris-tablet-dan-tinggi-baris | Pemotongan Badge, Klik Area Baris, Scrollbar Tablet, dan Tinggi Baris | 8-13 | E | resize viewport desktop (langkah 8, 13); verifikasi setelah resize viewport desktop (langkah 9-12) | - |
| TC-FA-CF-E2E-010-mobile-android-card-list-bottom-sheet-dan-selection-mode | Mobile Android: Card List, Tooltip Disabled, Bottom Sheet, dan Selection Mode | 1-35 | E | surface mobile/Android (spec mobile/Android) | - |
| TC-FA-CF-E2E-110-setup-column-pin-dan-unpin | Setup Column: Pin dan Unpin Tiap Kolom | 11-14 | E | resize viewport desktop (langkah 11, 14); verifikasi setelah resize viewport desktop (langkah 12-13) | - |
| TC-FA-CF-E2E-122-changelog-setup-column | Modal Changelog: Setup Column dan Isolasi dari Tabel Utama | 20-21, 24-25 | E | resize viewport desktop (langkah 20, 25); verifikasi setelah resize viewport desktop (langkah 21, 24) | - |

## Ragu / Perlu Konfirmasi

| Spek | Langkah | Catatan |
|---|---|---|
| (seluruh modul) | - | Persona semua langkah diasumsikan Principal karena tidak ada akun Distributor atau Partner di spek modul ini. Konfirmasi tipe company akun Total Control dan akun role lainnya. |
