# Eliminasi Step: Fixed Asset > AssetClass

Modul: AssetClass
Sumber: specs/FixedAsset/AssetClass
Tanggal: 2026-11-14

## Kriteria

- **A. Persona Distributor atau Partner**: tidak dipicu. Akun login di seluruh spek modul ini adalah akun Total Control atau akun role pada company Principal (pola `totalControl_*`, `readOnly_*`, `groupManager_*`, dst.). Tidak ditemukan spek yang login, logout, atau ganti akun ke akun Distributor atau Partner. Kata Distributor atau Partner yang muncul hanya sebagai nama data (Plan Owner) dicatat di Ragu. Asumsi persona Principal untuk semua langkah lain perlu dikonfirmasi (lihat Ragu).
- **B. Halaman detail**: hanya mencakup halaman detail user di Admin Console > Settings > User List (termasuk tab dan sub-tab di dalamnya) dan halaman detail client di Admin Console > Client List, termasuk aksi yang masuk ke halaman itu (klik Name, menu Detail). Detail user di Fixed Asset > Settings > User, detail user di Global Settings > User, detail aset, dan detail lain di Fixed Asset (Role, Asset Name, Group, Class, mode Edit) bukan B dan dipertahankan. Tidak ditemukan langkah di spek modul ini yang membuka atau beroperasi di halaman detail user atau client Admin Console (langkah yang menyebut Admin Console hanya menyangkut Role & Permission, Activity Log, Plans & Licensing, atau aksi lewat sesi API atau fixture), sehingga B tidak dipicu.
- **C. Fitur AI**: tidak ada. Pencarian `AI`, `chatbot`, `OCR`, dan `asisten` di seluruh spek Fixed Asset tidak menemukan fitur AI.
- **D. Menu Approval**: hanya menu Approval di Admin Console (sidebar atau halaman Admin Console > Approvals, termasuk Tab Active dan History) dan langkah yang masuk atau beroperasi di dalamnya. Approval di Fixed Asset (menu, antrean, Submit for Approval, Waiting for Approval, Approve atau Reject lewat UI atau API) tidak dikecualikan. Sub-tab Pending Approvals pada Responsibilities detail user (Global Settings maupun Fixed Asset) tidak dikecualikan. Teks approval di dialog, TAG Log, dan notifikasi bukan D. Tidak ada langkah di modul ini yang masuk atau beroperasi di Admin Console > Approvals, sehingga D tidak dipicu.
- **E. Surface mobile atau Android, serta resize viewport desktop**: langkah yang menguji aplikasi Android, aplikasi mobile, bottom sheet, card list, atau long press dikecualikan. Semua langkah UI di spek berjudul `android` atau `mobile` dikecualikan, sedangkan langkah seed atau fixture API di spek tersebut dipertahankan. Penyebutan Android, Mobile App, atau Mobile sebagai nilai data (Device atau Browser, nama asset class) tidak dikecualikan. Langkah yang mengubah atau memulihkan ukuran viewport browser desktop (persempit, perkecil, atur lebar, kembalikan atau pulihkan viewport) dikecualikan dengan alasan resize viewport desktop. Langkah campuran (resize bersama aksi lain dalam satu langkah) dipertahankan dan dicatat di Ragu. Termasuk langkah verifikasi yang hanya ada karena resize itu (gulir horizontal, kolom beku, layout viewport sempit, walkthrough tertutup saat resize).

Catatan metode: himpunan langkah dikecualikan dihitung ulang dari spek sebagai A, B, C, D, E (D hanya menu Approval di Admin Console; E termasuk resize viewport desktop). Klasifikasi memakai aturan teks (pencarian) dan pemeriksaan langkah yang menyebut Admin Console > Approvals serta langkah resize viewport. Ini bukan pembacaan manual setiap langkah, sehingga perlu verifikasi sampling sebelum eliminasi dijalankan.

Ringkasan: 2 spek punya eliminasi, 4 dari 6882 langkah bernomor dikecualikan, 1 item di Ragu.

## Daftar Eliminasi

| Spek | Judul | Langkah dikecualikan | Kriteria | Alasan | Dependensi |
|---|---|---|---|---|---|
| TC-FA-FAAC-E2E-017-aksesibilitas-label-dan-responsif-tablet | Aksesibilitas Label Toggle, Ikon Accounts, dan Tab Detail serta Tampilan Responsif Tabel dan Form pada Lebar Tablet | 25-27, 30-31 | E | resize viewport desktop (langkah 25, 31); verifikasi setelah resize viewport desktop (langkah 26-27, 30) | - |
| TC-FA-FAAC-E2E-153-changelog-setup-column-ceklis-geser-dan-pin | Modal Changelog: Setup Column Ceklis Kolom, Geser Urutan Kolom, dan Pin serta Unpin Kolom | 29-31, 36-38 | E | resize viewport desktop (langkah 29, 38); verifikasi setelah resize viewport desktop (langkah 30-31, 36-37) | - |

## Ragu / Perlu Konfirmasi

| Spek | Langkah | Catatan |
|---|---|---|
| (seluruh modul) | - | Persona semua langkah diasumsikan Principal karena tidak ada akun Distributor atau Partner di spek modul ini. Konfirmasi tipe company akun Total Control dan akun role lainnya. |
| TC-FA-FAAC-E2E-123-setup-column-geser-dan-pin | 16, 21, 26, 29 | Menggeser tabel pada lebar layar sempit tanpa langkah resize viewport eksplisit di spek (tidak ada langkah yang mengubah viewport); dipertahankan, konfirmasi |
