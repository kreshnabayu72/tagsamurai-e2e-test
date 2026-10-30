---
id: TC-GS-TAG-E2E-032-commit-kolisi-waiting-for-approval-dan-auto-switch-jalur-a
title: "Commit: Self-Purchased Bertabrakan In Use Client Lain (Waiting for Approval, Dialog 8) dan Auto-Switch ke Jalur A"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-100
  - TC-GS-TAG-167
coverage:
  web: automated
---

# Commit: Self-Purchased Bertabrakan In Use Client Lain (Waiting for Approval, Dialog 8) dan Auto-Switch ke Jalur A

## Prerequisites

- Mode: FE+BE (backend nyata; pemicu Admin Console memakai sesi API, P-2).
- Akun aktor: Total Control Client A Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Tidak ada sesi UI kedua.
- Pelaku kedua (sesi API, hanya memicu perubahan state): Principal pada Admin Console yang menambahkan unit stok resmi (TC-GS-TAG-167). Akun pelaku tidak tertulis di TC; disediakan tim FE (S-13). Pre-setup TC mencatat Principal approver `principalApprover_automated@qwertysystem.net` (`Spectra.env.GS_PRINCIPAL_TC_PASSWORD`) tetapi tidak menyatakannya untuk menambah stok (Q-2).
- Data Pre-setup (dipulihkan lewat fixture BE sebelum spec dan antar blok): Client A GPS terpakai 1 dari 30 (Seed Registri A); opsi mandiri Client A aktif; katalog Client A memuat Device Name `Queclink GV300` (Brand `Queclink`, Model/Type `GV300`, aktif) dan `Teltonika FMB920` (Brand `Teltonika`, Model/Type `FMB920`). IMEI `356938035643201` (DD-N4) aktif In Use di Client B (milik Total Control Client B Kartika Sari `totalControl_automated_qaTeam2@qwertysystem.net`, `Spectra.env.GS_CLIENTB_TC_PASSWORD`; hanya fixture BE, tidak login). IMEI `356938035643101` (DD-N1) tidak ada di stok maupun registri; unit stok resminya ditambahkan oleh pelaku kedua pada TC-GS-TAG-167.
- Kemampuan teknis (disediakan tim FE/BE): seed/reset unit Client B, stok resmi Client A, dan registri Client A; sesi API Admin Console untuk menambah unit stok resmi; label dan placeholder input entri manual GPS serta tombol `Add` menunggu desain (NC-11), selektor disediakan tim FE.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): hapus unit stok resmi `356938035643101` yang ditambahkan, pulihkan registri Client A dan unit Client B, buang staging yang tersisa.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain stok yang dipulihkan. Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-TAG-100: Self-Purchased bertabrakan dengan unit In Use client lain

1. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
2. Isi Template Device Name `Queclink GV300`, Brand `Queclink`
3. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643201`
4. Klik [Submit], lalu klik [Submit] pada dialog
5. Verifikasi toast sukses: "Success, TAG has been activated."
6. Verifikasi dialog informasi "Your activation is pending review." tampil
7. Verifikasi baris `356938035643201` keluar dari staging
8. Tutup dialog informasi "Your activation is pending review." (kontrol penutup disediakan tim FE)
9. Klik item sidebar `TAG`, klik Tab All, ketik Search `356938035643201`, tekan Enter
10. Verifikasi `356938035643201` berstatus `Waiting for Approval` di registri
11. Verifikasi kartu GPS `2 of 30`
12. Pulihkan registri Client A dan unit Client B ke kondisi awal lewat fixture BE

### TC-GS-TAG-167: Self-Purchased yang ternyata cocok stok resmi saat commit auto-switch ke Jalur A

13. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
14. Isi Template Device Name `Queclink GV300`, Brand `Queclink`
15. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643101` (tidak ada di stok saat ditambahkan)
16. Dari Admin Console (sesi API pelaku kedua) tambahkan `356938035643101` sebagai unit stok resmi Device Name `Teltonika FMB920` hingga tersimpan
17. Klik [Submit], lalu klik [Submit] pada dialog
18. Verifikasi toast info: "Matched to your official stock — details updated automatically."
19. Verifikasi toast sukses: "Success, TAG has been activated." tampil berdampingan dengan toast info
20. Klik item sidebar `TAG`, klik Tab All, ketik Search `356938035643101`, tekan Enter
21. Verifikasi `356938035643101` bersumber Official
22. Verifikasi Device Name `356938035643101` bernilai `Teltonika FMB920` (menimpa Template `Queclink GV300`)

## Notes

- Mode: FE+BE. P-2: pelaku kedua hanya memicu perubahan state lewat sesi API (langkah 16 ditulis "hingga ... tersimpan"); hasilnya diasersi di sesi Client A, bukan di sesi pelaku. Client B hanya fixture (unit In Use), tanpa sesi UI.
- Langkah penghubung (tanpa `Verifikasi`, S-03): 1, 8, 9, 12, 13, 20 (membuka sesi, menutup dialog informasi sebelum navigasi, pindah ke registri dan Search untuk menemukan baris target, pemulihan); 16 adalah pemicu state dari TC.
- Langkah 5 dan 6 diasersi berurutan (toast lalu dialog) sesuai urutan Expected TC-GS-TAG-100 butir a.
- Pembagian TC lintas spec: TC-GS-TAG-99 dan 101 (commit sukses tanpa kolisi) berada di spec 031.
- Temuan untuk QA:
  - TC-GS-TAG-100: judul dan tombol Dialog 8 (`Your activation is pending review.`) tidak ditulis di TC; spec hanya mengasersi teksnya dan menutupnya (langkah 8) dengan kontrol penutup yang disediakan tim FE sebelum navigasi ke registri.
  - TC-GS-TAG-167 (Q-5): pemicu "unit stok resmi ditambahkan sebelum Submit" memakai sesi API pelaku kedua; mekanismenya disediakan tim FE/BE. Akun pelaku tidak tertulis (Q-2).
  - TC-GS-TAG-167 Expected a menyebut "Official dengan Device Name `Teltonika FMB920`" tetapi tidak menyebut Brand dan Model/Type hasil override; spec hanya mengasersi Source dan Device Name.
  - Post Condition TC-GS-TAG-100 (butir a sampai c: status Waiting for Approval, Subject Activation Collision di Approvals > TAG Stock, Event Log Waiting for Approval 1) hanya butir a yang punya padanan Expected (langkah 10); butir b dan c tidak diasersi karena tanpa langkah observasi.
