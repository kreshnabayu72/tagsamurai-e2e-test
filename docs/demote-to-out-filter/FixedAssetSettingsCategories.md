# Eliminasi Step: Fixed Asset > SettingsCategories

Modul: SettingsCategories
Sumber: specs/FixedAsset/SettingsCategories
Tanggal: 2026-11-14

## Kriteria

- **A. Persona Distributor atau Partner**: tidak dipicu. Akun login di seluruh spek modul ini adalah akun Total Control atau akun role pada company Principal (pola `totalControl_*`, `readOnly_*`, `groupManager_*`, dst.). Tidak ditemukan spek yang login, logout, atau ganti akun ke akun Distributor atau Partner. Kata Distributor atau Partner yang muncul hanya sebagai nama data (Plan Owner) dicatat di Ragu. Asumsi persona Principal untuk semua langkah lain perlu dikonfirmasi (lihat Ragu).
- **B. Halaman detail**: hanya mencakup halaman detail user di Admin Console > Settings > User List (termasuk tab dan sub-tab di dalamnya) dan halaman detail client di Admin Console > Client List, termasuk aksi yang masuk ke halaman itu (klik Name, menu Detail). Detail user di Fixed Asset > Settings > User, detail user di Global Settings > User, detail aset, dan detail lain di Fixed Asset (Role, Asset Name, Group, Class, mode Edit) bukan B dan dipertahankan. Tidak ditemukan langkah di spek modul ini yang membuka atau beroperasi di halaman detail user atau client Admin Console (langkah yang menyebut Admin Console hanya menyangkut Role & Permission, Activity Log, Plans & Licensing, atau aksi lewat sesi API atau fixture), sehingga B tidak dipicu.
- **C. Fitur AI**: tidak ada. Pencarian `AI`, `chatbot`, `OCR`, dan `asisten` di seluruh spek Fixed Asset tidak menemukan fitur AI.
- **D. Menu Approval**: hanya menu Approval di Admin Console (sidebar atau halaman Admin Console > Approvals, termasuk Tab Active dan History) dan langkah yang masuk atau beroperasi di dalamnya. Approval di Fixed Asset (menu, antrean, Submit for Approval, Waiting for Approval, Approve atau Reject lewat UI atau API) tidak dikecualikan. Sub-tab Pending Approvals pada Responsibilities detail user (Global Settings maupun Fixed Asset) tidak dikecualikan. Teks approval di dialog, TAG Log, dan notifikasi bukan D. Tidak ada langkah di modul ini yang masuk atau beroperasi di Admin Console > Approvals, sehingga D tidak dipicu.
- **E. Surface mobile atau Android, serta resize viewport desktop**: langkah yang menguji aplikasi Android, aplikasi mobile, bottom sheet, card list, atau long press dikecualikan. Semua langkah UI di spek berjudul `android` atau `mobile` dikecualikan, sedangkan langkah seed atau fixture API di spek tersebut dipertahankan. Penyebutan Android, Mobile App, atau Mobile sebagai nilai data (Device atau Browser, nama asset class) tidak dikecualikan. Langkah yang mengubah atau memulihkan ukuran viewport browser desktop (persempit, perkecil, atur lebar, kembalikan atau pulihkan viewport) dikecualikan dengan alasan resize viewport desktop. Langkah campuran (resize bersama aksi lain dalam satu langkah) dipertahankan dan dicatat di Ragu. Termasuk langkah verifikasi yang hanya ada karena resize itu (gulir horizontal, kolom beku, layout viewport sempit, walkthrough tertutup saat resize).

Catatan metode: himpunan langkah dikecualikan dihitung ulang dari spek sebagai A, B, C, D, E (D hanya menu Approval di Admin Console; E termasuk resize viewport desktop). Klasifikasi memakai aturan teks (pencarian) dan pemeriksaan langkah yang menyebut Admin Console > Approvals serta langkah resize viewport. Ini bukan pembacaan manual setiap langkah, sehingga perlu verifikasi sampling sebelum eliminasi dijalankan.

Ringkasan: 7 spek punya eliminasi, 41 dari 6452 langkah bernomor dikecualikan, 0 item di Ragu.

## Daftar Eliminasi

| Spek | Judul | Langkah dikecualikan | Kriteria | Alasan | Dependensi |
|---|---|---|---|---|---|
| TC-FA-CAT-E2E-004-sidebar-collapse-state-tersimpan-tablet-aksesibilitas | Sidebar Collapse, State Tersimpan, Viewport Tablet, dan Aksesibilitas Pohon Kategori | 18-21 | E | resize viewport desktop (langkah 18, 20); verifikasi setelah resize viewport desktop (langkah 19, 21) | - |
| TC-FA-CAT-E2E-007-guided-tooltip-categories-walkthrough | Guided Tooltip Categories: Kunjungan Pertama, Navigasi, dan Flag Seen | 37-41 | E | resize viewport desktop (langkah 37, 39); verifikasi setelah resize viewport desktop (langkah 38, 40-41) | - |
| TC-FA-CAT-E2E-010-mobile-android-card-list-bottom-sheet-selection-walkthrough | Mobile Android: Card List, Bottom Sheet Tree, Selection Mode, dan Walkthrough | 1-33 | E | surface mobile/Android (spec mobile/Android) | - |
| TC-FA-CAT-E2E-104-setup-column-tabel-utama-pin-dan-batas-pin-keempat | Setup Column Tabel Utama: Pin Kolom Membekukan Kolom saat Scroll Horizontal dan Batas Pin Keempat | 1, 5-6, 8, 12-13 | E | resize viewport desktop (langkah 1); verifikasi setelah resize viewport desktop (langkah 5-6, 8, 12-13) | - |
| TC-FA-CAT-E2E-120-modal-changelog-pin-dan-unpin-kolom-persist | Modal Changelog: Pin dan Unpin Tujuh Kolom Lewat Popup Setup Column dengan Persist | 1, 4-5, 7, 9 | E | resize viewport desktop (langkah 1); verifikasi setelah resize viewport desktop (langkah 4-5, 7, 9) | - |
| TC-FA-CAT-E2E-129-tabel-assets-detail-setup-column-pin-unpin-tujuh-kolom-dan-guard-satu-kolom | Tabel Assets pada Popup Detail: Pin dan Unpin Tujuh Kolom lewat Setup Column dengan Persist serta Guard Satu Kolom Tersisa | 1, 5-6, 8, 10 | E | resize viewport desktop (langkah 1); verifikasi setelah resize viewport desktop (langkah 5-6, 8, 10) | - |
| TC-FA-CAT-E2E-130-kolom-label-tabel-assets-setup-column-geser-dan-pin | Kolom Curated Label pada Tabel Assets: Default Tersembunyi, Ceklis, Geser Urutan, dan Pin dengan Persist | 1, 22-23, 25 | E | resize viewport desktop (langkah 1); verifikasi setelah resize viewport desktop (langkah 22-23, 25) | - |

## Ragu / Perlu Konfirmasi

| Spek | Langkah | Catatan |
|---|---|---|
| (seluruh modul) | - | Persona semua langkah diasumsikan Principal karena tidak ada akun Distributor atau Partner di spek modul ini. Konfirmasi tipe company akun Total Control dan akun role lainnya. |
| TC-FA-CAT-E2E-104-setup-column-tabel-utama-pin-dan-batas-pin-keempat | 14 | Langkah pengulangan memuat gulir dan verifikasi pin untuk kolom lain dalam satu langkah; langkah campuran dipertahankan, konfirmasi |
