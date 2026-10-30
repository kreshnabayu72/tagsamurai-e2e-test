---
id: TC-GS-UCF-E2E-058-download-di-atas-5000-baris-loading-screen
title: "Download di Atas 5.000 Baris Tabel Custom Field: Loading Screen sampai Berkas Siap lalu Langsung Terunduh"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UCF-365
coverage:
  web: automated
---

# Download di Atas 5.000 Baris Tabel Custom Field: Loading Screen sampai Berkas Siap lalu Langsung Terunduh

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Client Limit (Wulan Sari) `totalControl_automated_qaTeam4@qwertysystem.net`. Login sekali di hook `before` spec ini dengan `Spectra.env.GS_LIMIT_TC_PASSWORD`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data (kelas volume data, e): Client Limit memiliki tepat 5.001 Custom Field dan Master Data Count Limit Client Limit 10.000 (volume dan limit diatur backend sebelum spec; disediakan tim BE, TC tidak menyebut mekanismenya). Pre-setup Client Limit mencatat Master Data Count Limit 1.000 dan 999 Custom Field `Lim 001` sampai `Lim 999`; spec ini membutuhkan kondisi 10.000 dan 5.001 dan dipulihkan oleh backend sesudah spec (hook `after`). Seluruh field adalah precondition TC, tidak diasersi satu per satu; fixture baru `Fixture.customFieldUser.volume365`.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field (Client Limit); spec tidak menguji navigasi sehingga tidak mengulang langkah buka di `## Test Steps`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): minta backend mengembalikan volume Custom Field dan Master Data Count Limit Client Limit ke nilai awal (Post Condition TC); hapus berkas hasil unduhan dari direktori unduhan uji; kembalikan sesi ke akun default suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_<page_key>` halaman Custom Field true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: menangkap berkas hasil unduhan browser dan menghitung baris isinya (baris header dan 5.001 baris data); mendeteksi loading screen, toast (sukses dan informasional), dan notifikasi in-app; membaca keberadaan job background (state backend yang tidak terlihat di UI; disediakan tim FE/BE, tanpa mengarang endpoint).
- State global: tidak ada yang diubah oleh langkah; volume dan limit Client Limit diatur dan dipulihkan backend.

## Test Steps

### TC-GS-UCF-365: Download di atas 5.000 baris

1. Klik icon Download
2. Pilih opsi `Download as CSV`
3. Verifikasi loading screen tampil
4. Verifikasi tidak ada toast sukses
5. Verifikasi tidak ada toast informasional
6. Verifikasi tidak ada notifikasi in-app
7. Verifikasi berkas CSV langsung terunduh setelah loading screen
8. Verifikasi loading screen tidak tampil lagi setelah berkas terunduh
9. Buka berkas CSV hasil unduhan
10. Verifikasi berkas memuat baris header
11. Verifikasi berkas memuat 5.001 baris data
12. Verifikasi tidak ada job background yang dibuat untuk download ini

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas e (volume data): satu spec per jenis harness; volume 5.001 baris tidak lazim dihasilkan seed rutin.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 9 (membuka berkas hasil unduhan agar isinya dapat diasersi).
- Asersi absence atas state sementara (langkah 4, 5, dan 6) ditaruh segera sesudah pemicu (klik `Download as CSV`) dan sebelum asersi berkas (bagian 8b butir 11); loading screen pada langkah 3 diasersi sebelum langkah yang mengubah state-nya (butir 5). Pemicu pada langkah 2 menjadi anchor positif yang buktinya menyusul pada langkah 7 (berkas terunduh). Langkah 12 (absence job background) ditaruh sesudah berkas terunduh karena job background adalah state backend dan bukan state sementara UI.
- Pembagian TC lintas spec: Download tabel utama pada volume normal (TC-GS-UCF-244 sampai 250, 252) ada di spec 057; kegagalan Download (TC-GS-UCF-251 dan 552) di spec 060.
- Temuan untuk QA:
  - TC-GS-UCF-365 tidak menyebut nama berkas; spec tidak mengasersi nama berkas. TC juga tidak menyebut cara memeriksa "tidak ada notifikasi atau job background" (UI notifikasi dan state job di backend); asersi notifikasi memakai pembacaan UI notifikasi, sedangkan pembacaan job background disediakan tim FE/BE tanpa mengarang endpoint.
  - Precondition TC menyebut Master Data Count Limit Client Limit 10.000, sedangkan Tabel Pre-setup TC mencatat Client Limit dengan limit 1.000 dan 999 field; kondisi 10.000 dan 5.001 field diatur backend khusus untuk TC ini.
  - Post Condition TC ("Volume dan Master Data Count Limit Client Limit dikembalikan backend") tidak punya langkah observasi; tidak diasersi, pemulihan dilakukan di hook `after`.
  - Selection Limit dan Master Data Count Limit Client Limit dipakai juga oleh TC lain (TC-GS-UCF-145, 146, 435, 454); spec ini membutuhkan volume 5.001 sehingga tidak boleh berjalan bersamaan dengan spec Client Limit lain (suite serial).
