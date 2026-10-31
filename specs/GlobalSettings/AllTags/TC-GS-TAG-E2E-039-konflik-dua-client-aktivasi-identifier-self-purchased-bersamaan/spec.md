---
id: TC-GS-TAG-E2E-039-konflik-dua-client-aktivasi-identifier-self-purchased-bersamaan
title: "Konflik Dua Client: Aktivasi Identifier Self-Purchased Baru yang Sama Bersamaan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-TAG-186
coverage:
  web: automated
---

# Konflik Dua Client: Aktivasi Identifier Self-Purchased Baru yang Sama Bersamaan

## Prerequisites

- Mode: FE+BE (backend nyata; pelaku Client B lewat sesi API aktor).
- Akun aktor:
  - Total Control Client A Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; satu-satunya sesi UI.
  - Total Control Client B Kartika Sari `totalControl_automated_qaTeam2@qwertysystem.net`, `Spectra.env.GS_CLIENTB_TC_PASSWORD`. Konteks kedua berupa sesi API yang hanya memicu perubahan state (aktivasi Self-Purchased hingga Activated); hasil di sisi Client B tidak diasersi, sehingga tidak butuh sesi UI kedua.
- Data Pre-setup (dipulihkan lewat fixture BE sebelum spec): opsi mandiri aktif untuk Client A dan Client B; IMEI `356938035643101` (DD-N1) belum ada di stok maupun registri keduanya; katalog Client A memuat Device Name `Queclink GV300` (Brand `Queclink`).
- Sesi API aktor (kemampuan dinyatakan di `suite.md`): Total Control Client B memicu aktivasi Self-Purchased (langkah 4).
- Kemampuan teknis (disediakan tim FE/BE): kontrol penutup dialog informasi "Your activation is pending review."; sesi API Client B untuk aktivasi Self-Purchased; seed/reset registri dan stok kedua client; label dan placeholder input entri manual GPS serta tombol `Add` menunggu desain (NC-11), selektor disediakan tim FE.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): hapus `356938035643101` dari registri Client B dan Client A, pulihkan stok, buang staging yang tersisa.
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Suite serial (`parallel: false`). Spec tidak mengubah state global. Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-TAG-186: Dua client mengaktifkan identifier Self-Purchased baru yang sama bersamaan

1. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
2. Isi Template Device Name `Queclink GV300`, Brand `Queclink`
3. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643101`
4. Dari sesi Client B (sesi API), aktivasi `356938035643101` hingga Activated tersimpan
5. Klik [Submit], lalu klik [Submit] pada dialog (konfirmasi)
6. Verifikasi toast sukses: "Success, TAG has been activated."
7. Verifikasi dialog informasi "Your activation is pending review." tampil
8. Verifikasi baris `356938035643101` tidak berstatus `Failed` di staging
9. Tutup dialog informasi "Your activation is pending review." (kontrol disediakan tim FE)
10. Klik item sidebar `TAG`, klik Tab All, ketik Search `356938035643101`, tekan Enter
11. Verifikasi `356938035643101` Client A berstatus `Waiting for Approval`

## Notes

- Mode: FE+BE. Konteks Client B adalah pelaku kedua lewat sesi API aktor yang hanya memicu state (langkah 4 ditulis "hingga ... tersimpan"); hasil diasersi di sesi Client A. Spec ini satu-satunya spec konflik dua tenant untuk TC ini.
- Langkah penghubung (tanpa `Verifikasi`, S-03): 1, 9, 10 (membuka sesi, menutup dialog informasi, pindah ke registri dan Search untuk menemukan baris target); langkah 4 adalah pemicu state dari TC.
- Pembagian TC lintas spec: TC-GS-TAG-100 dan 167 (kolisi Self-Purchased dengan unit In Use dan auto-switch) berada di spec 032.
- Temuan untuk QA:
  - Q-5: pemicu "bersamaan" (TC-GS-TAG-186) tidak deterministik; spec mengaktivasi dari Client B sebelum Submit Client A, dan mekanismenya disediakan tim FE/BE.
  - TC-GS-TAG-186 Expected hanya memuat satu butir majemuk (Waiting for Approval bukan Failed, toast sukses, dialog); spec memecahnya menjadi langkah 6, 7, 8, dan 11 satu klausa per `Verifikasi`.
  - Dialog informasi "Your activation is pending review.": judul dan tombol penutupnya tidak ditulis di TC; spec menutupnya (langkah 9) sebelum navigasi dengan kontrol yang disediakan tim FE.
  - Post Condition bernilai `-`.
