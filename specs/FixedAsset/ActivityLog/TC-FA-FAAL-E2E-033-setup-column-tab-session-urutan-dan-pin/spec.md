---
id: TC-FA-FAAL-E2E-033-setup-column-tab-session-urutan-dan-pin
title: "Setup Column Tab Session: Drag Urutan dan Pin/Unpin Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-110
  - TC-FA-FAAL-111
coverage:
  web: automated
---

# Setup Column Tab Session: Drag Urutan dan Pin/Unpin Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Admin Alpha, Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log, Tab Session). Tidak ada ganti akun di tengah spec.
- Data Pre-setup #11 (Tab Session SS-01 sampai SS-11), hanya dibaca dan tidak diubah. Spec ini mengasersi kolom, bukan isi baris tertentu. Fixture `fixtures/activity-log.json` disediakan tim FE (nama kunci ditetapkan tim FE).
- Kemampuan teknis: drag and drop baris pada popup Setup Column dan guliran horizontal tabel.
- Kolom untuk langkah berulang (langkah 1 sampai 10 dan langkah 11 sampai 23; Data Uji TC-FA-FAAL-110 dan 111):

  | Kolom |
  |---|
  | `Date` |
  | `User` |
  | `Employee ID` |
  | `Position` |
  | `Division` |
  | `Activity` |
  | `Status` |
  | `Note` |
  | `IP Address` |
  | `Device/Browser` |

- State yang diubah spec: konfigurasi kolom Tab Session (urutan dan pin, disimpan lewat `[Save]`). Langkah 9 dan 10 serta langkah 20 sampai 21 mengembalikan konfigurasi tiap iterasi; hook `after` memulihkannya dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Flag Guided Tooltip halaman Activity Log di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-110: Ubah urutan kolom Tab Session lewat drag di Popup Setup Column

Untuk setiap baris tabel Prerequisites "Kolom untuk langkah berulang" (langkah 1 sampai 10):

1. Klik header kolom Actions (⋯) > `Setup Column...`
2. Drag kolom ke posisi paling atas
3. Verifikasi kolom menjadi kolom pertama di Live Preview
4. Klik `[Save]`
5. Verifikasi kolom menjadi kolom pertama di tabel
6. Tekan F5
7. Verifikasi kolom tetap menjadi kolom pertama di tabel setelah muat ulang
8. Klik header kolom Actions (⋯) > `Setup Column...`
9. Klik `[Reset to Default]`
10. Klik `[Save]`

### TC-FA-FAAL-111: Pin dan unpin kolom Tab Session lewat Popup Setup Column

Untuk setiap baris tabel Prerequisites "Kolom untuk langkah berulang" (langkah 11 sampai 23):

11. Klik header kolom Actions (⋯) > `Setup Column...`
12. Klik icon Pin pada kolom
13. Klik `[Save]`
14. Gulir tabel secara horizontal
15. Verifikasi kolom tetap terlihat di sisi kiri saat tabel digulir horizontal
16. Tekan F5
17. Gulir tabel secara horizontal
18. Verifikasi kolom tetap beku setelah muat ulang
19. Klik header kolom Actions (⋯) > `Setup Column...`
20. Klik icon Pin pada kolom lagi untuk unpin
21. Klik `[Save]`
22. Gulir tabel secara horizontal
23. Verifikasi kolom ikut bergulir setelah unpin

## Notes

- Alasan di atas 35 langkah dengan ekspansi (23 langkah nominal; langkah 1 sampai 10 dan 11 sampai 23 masing-masing diulang untuk 10 kolom sehingga 230 langkah): kedua TC satu halaman, satu dataset #11, dan satu kelas fungsional (Setup Column), dan masing-masing TC adalah satu TC dengan 10 iterasi yang tidak dapat dipecah (satu TC tetap satu spec); tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah berulang mengikuti idiom "Untuk setiap baris tabel" (butir 8b.7); `Verifikasi` tetap satu per klausa.
- Langkah penghubung (S-03): langkah 17 (menggulir tabel lagi setelah muat ulang agar asersi "tetap beku" pada langkah 18 diamati pada keadaan guliran, S-14); langkah 22 (menggulir tabel agar asersi "ikut bergulir" pada langkah 23 diamati pada keadaan guliran, S-14); langkah 8 dan 19 (membuka kembali popup setelah muat ulang, sesuai urutan TC).
- Konfigurasi tiap iterasi TC-FA-FAAL-110 dipulihkan lewat `[Reset to Default]` dan `[Save]` (langkah 9 dan 10) sesuai TC; TC-FA-FAAL-111 memulihkan pin lewat unpin (langkah 20 dan 21) sesuai TC.
- Temuan untuk QA:
  - TC-FA-FAAL-110 dan 111 menulis "muat ulang halaman" tanpa menyebut cara; spec memakai F5.
  - TC-FA-FAAL-110 dan 111 tidak menyebut keadaan guliran horizontal setelah muat ulang; spec menggulir tabel lagi sebelum mengasersi kolom beku (langkah 17).
  - TC-FA-FAAL-110 mengharapkan kolom `Date` menjadi kolom pertama setelah di-drag ke posisi paling atas padahal `Date` sudah berposisi pertama pada urutan bawaan; spec mengikuti TC.
  - TC-FA-FAAL-111 pada Expected tidak menyebut perilaku pin untuk kolom yang pada viewport uji tidak memerlukan guliran horizontal; spec mengasumsikan viewport uji cukup sempit sehingga tabel dapat digulir horizontal (kemampuan viewport disediakan tim FE).
