---
id: TC-FA-LBL-E2E-037-validasi-label-name-edit-kosong-spasi-panjang-trim-dan-emoji-bagian-1
title: "Validasi Label Name Edit: Kosong, Spasi, Panjang, Trim, dan Emoji (bagian 1/2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-114
  - TC-FA-LBL-115
  - TC-FA-LBL-117
  - TC-FA-LBL-123
  - TC-FA-LBL-124
  - TC-FA-LBL-485
coverage:
  web: automated
---

# Validasi Label Name Edit: Kosong, Spasi, Panjang, Trim, dan Emoji (bagian 1/2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept. Tidak ada kasus di spec ini yang menyimpan perubahan.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-037`):
  - `Edit Target 114 {runId}-037` (satu label seed untuk keenam TC; modal dibuka sekali dan field dikembalikan di antara kasus)
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.tigaSpasi` | tiga karakter spasi |
  | `Fixture.assetLabeling.nama121` | 19 kata `Alpha` + `Delta12` dipisah spasi tunggal (121 karakter) |
  | `Fixture.assetLabeling.emoji` | `😊` |
  | `Fixture.assetLabeling.promoEmoji` | `Promo 😊` |
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |

- Kemampuan teknis: mengetik dan menempel (clipboard) teks beremoji ke field, menyuntikkan nilai langsung ke DOM field Label Name (TC-FA-LBL-124, disediakan tim FE), hover tombol, dan menekan Enter.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed milik spec (termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search `Edit Target 114 {runId}-037`, tekan Enter
2. Klik `⋯` pada baris `Edit Target 114 {runId}-037`, lalu klik `Edit`

### TC-FA-LBL-114: Mengosongkan Label Name pada Edit membuat Save disabled dengan tooltip

3. Hapus seluruh isi Label Name
4. Hover `[Save]`
5. Verifikasi `[Save]` berstatus disabled
6. Verifikasi tooltip `Enter a label name to continue.` tampil

### TC-FA-LBL-115: Label Name hanya berisi spasi pada Edit dianggap kosong

7. Ganti isi Label Name dengan `Fixture.assetLabeling.tigaSpasi`
8. Hover `[Save]`
9. Verifikasi `[Save]` berstatus disabled dengan tooltip `Enter a label name to continue.`

### TC-FA-LBL-117: Edit nama 121 karakter menampilkan V-02 dan Save disabled

10. Ganti isi Label Name dengan `Fixture.assetLabeling.nama121`
11. Hover `[Save]`
12. Verifikasi inline error `Max. 120 characters` tampil real-time
13. Verifikasi `[Save]` berstatus disabled dengan tooltip `Max. 120 characters`

### TC-FA-LBL-123: Edit: emoji diblok di level input

14. Ganti isi Label Name dengan `Edit Target 114 {runId}-037` (kembalikan ke nilai tersimpan)
15. Ketik `Fixture.assetLabeling.emoji` di akhir Label Name
16. Verifikasi emoji tidak masuk ke field Label Name
17. Verifikasi tidak ada pesan error pada Label Name
18. Tempel `Fixture.assetLabeling.promoEmoji` dari clipboard di Label Name
19. Verifikasi emoji tidak masuk ke field Label Name
20. Verifikasi tidak ada pesan error pada Label Name

### TC-FA-LBL-124: Edit: emoji yang lolos filter memunculkan fallback V-08

21. Injeksi nilai `Fixture.assetLabeling.promoEmoji` langsung ke DOM field Label Name
22. Hover `[Save]`
23. Verifikasi inline error `Label name contains invalid characters` tampil langsung
24. Verifikasi `[Save]` berstatus disabled dengan tooltip `Label name contains invalid characters`

### TC-FA-LBL-485: Edit: Enter pada Label Name kosong menampilkan pesan fallback V-01 tanpa menyimpan

25. Hapus seluruh isi Label Name
26. Klik Label Name, lalu tekan Enter
27. Verifikasi inline error `Label name must not be empty` tampil di bawah Label Name
28. Verifikasi modal Edit Label tetap terbuka
29. Verifikasi tidak ada toast
30. Ganti isi Label Name dengan `Edit Target 114 {runId}-037` (kembalikan ke nilai tersimpan)
31. Klik icon `[✕]`
32. Verifikasi baris `Edit Target 114 {runId}-037` tampil dengan nama tidak berubah

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 3b (Edit Label). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 adalah Search untuk menemukan baris label target pada Labels List; bukan bagian Expected TC.
- Langkah penghubung (S-03, S-09): langkah 14, 30, 31 mengembalikan Label Name ke nilai tersimpan (menghapus error kasus sebelumnya dan membuat form bersih) lalu menutup modal bersih dengan `[✕]`; form tidak berakhir dirty.
- Seeding minimal (S-11): keenam TC memakai satu label seed dan satu pembukaan modal karena tidak ada yang menyimpan (bagian 3, halaman yang sama dipakai berulang); Precondition "Label seed `Edit Target <nomor TC>`" tiap TC terpenuhi oleh label yang sama dengan nilai tersimpan identik (Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0). Nama diberi suffix `{runId}-<NNN>` (S-12).
- Penyimpangan urutan (S-05, bagian 3): TC-FA-LBL-485 ditaruh terakhir; urutan lain mengikuti nomor TC.
- Temuan untuk QA:
  - TC-FA-LBL-123 langkah 3 menempel `Promo 😊` tanpa menyebut apakah teks tanpa emoji (`Promo `) tetap masuk ke field; spec hanya mengasersi emoji tidak masuk dan tidak ada pesan error (Expected TC).
  - TC-FA-LBL-124 mensyaratkan injeksi nilai langsung ke DOM; mekanisme injeksi tidak disebut TC dan disediakan tim FE.
