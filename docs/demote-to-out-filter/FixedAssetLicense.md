# Eliminasi Step: Fixed Asset > License

Modul: License
Sumber: specs/FixedAsset/License
Tanggal: 2026-11-14

## Kriteria

- **A. Persona Distributor atau Partner**: tidak dipicu. Akun login di seluruh spek modul ini adalah akun Total Control atau akun role pada company Principal (pola `totalControl_*`, `readOnly_*`, `groupManager_*`, dst.). Tidak ditemukan spek yang login, logout, atau ganti akun ke akun Distributor atau Partner. Kata Distributor atau Partner yang muncul hanya sebagai nama data (Plan Owner) dicatat di Ragu. Asumsi persona Principal untuk semua langkah lain perlu dikonfirmasi (lihat Ragu).
- **B. Halaman detail**: hanya mencakup halaman detail user di Admin Console > Settings > User List (termasuk tab dan sub-tab di dalamnya) dan halaman detail client di Admin Console > Client List, termasuk aksi yang masuk ke halaman itu (klik Name, menu Detail). Detail user di Fixed Asset > Settings > User, detail user di Global Settings > User, detail aset, dan detail lain di Fixed Asset (Role, Asset Name, Group, Class, mode Edit) bukan B dan dipertahankan. Tidak ditemukan langkah di spek modul ini yang membuka atau beroperasi di halaman detail user atau client Admin Console (langkah yang menyebut Admin Console hanya menyangkut Role & Permission, Activity Log, Plans & Licensing, atau aksi lewat sesi API atau fixture), sehingga B tidak dipicu.
- **C. Fitur AI**: tidak ada. Pencarian `AI`, `chatbot`, `OCR`, dan `asisten` di seluruh spek Fixed Asset tidak menemukan fitur AI.
- **D. Menu Approval**: hanya menu Approval di Admin Console (sidebar atau halaman Admin Console > Approvals, termasuk Tab Active dan History) dan langkah yang masuk atau beroperasi di dalamnya. Approval di Fixed Asset (menu, antrean, Submit for Approval, Waiting for Approval, Approve atau Reject lewat UI atau API) tidak dikecualikan. Sub-tab Pending Approvals pada Responsibilities detail user (Global Settings maupun Fixed Asset) tidak dikecualikan. Teks approval di dialog, TAG Log, dan notifikasi bukan D. Tidak ada langkah di modul ini yang masuk atau beroperasi di Admin Console > Approvals, sehingga D tidak dipicu.
- **E. Surface mobile atau Android, serta resize viewport desktop**: langkah yang menguji aplikasi Android, aplikasi mobile, bottom sheet, card list, atau long press dikecualikan. Semua langkah UI di spek berjudul `android` atau `mobile` dikecualikan, sedangkan langkah seed atau fixture API di spek tersebut dipertahankan. Penyebutan Android, Mobile App, atau Mobile sebagai nilai data (Device atau Browser, nama asset class) tidak dikecualikan. Langkah yang mengubah atau memulihkan ukuran viewport browser desktop (persempit, perkecil, atur lebar, kembalikan atau pulihkan viewport) dikecualikan dengan alasan resize viewport desktop. Langkah campuran (resize bersama aksi lain dalam satu langkah) dipertahankan dan dicatat di Ragu. Termasuk langkah verifikasi yang hanya ada karena resize itu (gulir horizontal, kolom beku, layout viewport sempit, walkthrough tertutup saat resize).

Catatan metode: himpunan langkah dikecualikan dihitung ulang dari spek sebagai A, B, C, D, E (D hanya menu Approval di Admin Console; E termasuk resize viewport desktop). Klasifikasi memakai aturan teks (pencarian) dan pemeriksaan langkah yang menyebut Admin Console > Approvals serta langkah resize viewport. Ini bukan pembacaan manual setiap langkah, sehingga perlu verifikasi sampling sebelum eliminasi dijalankan.

Ringkasan: 10 spek punya eliminasi, 69 dari 5742 langkah bernomor dikecualikan, 3 item di Ragu.

## Daftar Eliminasi

| Spek | Judul | Langkah dikecualikan | Kriteria | Alasan | Dependensi |
|---|---|---|---|---|---|
| TC-FA-LIC-E2E-002-guided-tooltip-konten-skip-done-back-dan-overlay | Guided Tooltip: Konten, Back, Overlay, Resize, Skip, dan Done | 16-21 | E | resize viewport desktop (langkah 16, 18); verifikasi setelah resize viewport desktop (langkah 17, 19-21) | - |
| TC-FA-LIC-E2E-016-mobile-group-tree-drawer-session-card-card-list-dan-group | Mobile: Group Tree Drawer, Session Card, Card List, dan Group Quota Summary Scroll Horizontal | 1-24 | E | surface mobile/Android (spec mobile/Android) | - |
| TC-FA-LIC-E2E-017-mobile-filter-panel-bottom-sheet-toolbar-modal-sebagai | Mobile: Filter Panel Bottom Sheet, Toolbar, Modal sebagai Bottom Sheet, dan Banner | 1-25, 27-29, 31 | E | surface mobile/Android (spec mobile/Android) | - |
| TC-FA-LIC-E2E-066-subscription-history-setup-column-pin-reset-x-esc-satu | Subscription History: Setup Column (Pin dan Unpin per Kolom, Reset to Default, X atau Esc, dan Satu Kolom Tersisa) | 2, 6-7, 9-10, 14-15, 38 | E | resize viewport desktop (langkah 2, 38); verifikasi setelah resize viewport desktop (langkah 6-7, 9-10, 14-15) | - |
| TC-FA-LIC-E2E-075-allocation-history-setup-column-pin-reset-x-esc-satu | Allocation History: Setup Column (Pin dan Unpin per Kolom, Reset to Default, X atau Esc, dan Satu Kolom Tersisa) | 2, 6-7, 9-10, 14-15, 38 | E | resize viewport desktop (langkah 2, 38); verifikasi setelah resize viewport desktop (langkah 6-7, 9-10, 14-15) | - |
| TC-FA-LIC-E2E-083-active-sessions-setup-column-kolom-hideable-pin-reset-x | Active Sessions: Setup Column Pin dan Unpin, Reset to Default, X atau Esc, dan Satu Kolom Tersisa | 24, 27-28, 30, 32-33 | E | resize viewport desktop (langkah 24, 33); verifikasi setelah resize viewport desktop (langkah 27-28, 30, 32) | - |
| TC-FA-LIC-E2E-084-active-sessions-setup-column-kolom-curated-max-visible | Active Sessions: Setup Column Ceklis, Geser, dan Pin Kolom Curated Hidden Default | 22, 25-26, 28, 30, 32 | E | resize viewport desktop (langkah 22, 32); verifikasi setelah resize viewport desktop (langkah 25-26, 28, 30) | - |
| TC-FA-LIC-E2E-101-changelog-allocation-quota-setup-column-pin-reset-x-esc | Setup Column Modal Changelog Allocation Quota: Pin dan Unpin per Kolom, Reset to Default, Tutup X atau Esc, dan Satu Kolom Tersisa | 2, 5-6, 8, 11-14 | E | resize viewport desktop (langkah 2, 14); verifikasi setelah resize viewport desktop (langkah 5-6, 8, 11-13) | - |
| TC-FA-LIC-E2E-106-changelog-concurrent-user-setup-column-pin-dan-unpin | Setup Column Modal Changelog Concurrent User: Pin dan Unpin per Kolom dan Download CSV serta XLSX | 2, 5-6, 8, 11-14 | E | resize viewport desktop (langkah 2, 14); verifikasi setelah resize viewport desktop (langkah 5-6, 8, 11-13) | - |
| TC-FA-LIC-E2E-152-group-license-allocation-setup-column-pin-dan-unpin | Group License Allocation: Setup Column Pin dan Unpin Kolom Hideable Visible Default | 2, 5-6, 8, 10-11 | E | resize viewport desktop (langkah 2, 11); verifikasi setelah resize viewport desktop (langkah 5-6, 8, 10) | - |

## Ragu / Perlu Konfirmasi

| Spek | Langkah | Catatan |
|---|---|---|
| (seluruh modul) | - | Persona semua langkah diasumsikan Principal karena tidak ada akun Distributor atau Partner di spek modul ini. Konfirmasi tipe company akun Total Control dan akun role lainnya. |
| TC-FA-LIC-E2E-010-screening-sub-tab-subscription-history-kolom-isi-baris | 8 | Kata Distributor/Partner pada langkah sebagai nama data atau opsi (bukan persona login); A tidak dipicu, dipertahankan |
| TC-FA-LIC-E2E-011-screening-sub-tab-allocation-history-kolom-isi-baris | 8 | Kata Distributor/Partner pada langkah sebagai nama data atau opsi (bukan persona login); A tidak dipicu, dipertahankan |
| TC-FA-LIC-E2E-022-banner-renewal-isi-banner-successor-plan-owner-dan-term-terbaru | 9 | Kata Distributor/Partner pada langkah sebagai nama data atau opsi (bukan persona login); A tidak dipicu, dipertahankan |
