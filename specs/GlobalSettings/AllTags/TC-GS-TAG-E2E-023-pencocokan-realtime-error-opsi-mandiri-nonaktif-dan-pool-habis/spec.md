---
id: TC-GS-TAG-E2E-023-pencocokan-realtime-error-opsi-mandiri-nonaktif-dan-pool-habis
title: "Pencocokan Real-Time: Error T-10 saat Opsi Mandiri Nonaktif dan Error T-11 saat Pool Sesi Habis"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-TAG-63
  - TC-GS-TAG-64
coverage:
  web: automated
---

# Pencocokan Real-Time: Error T-10 saat Opsi Mandiri Nonaktif dan Error T-11 saat Pool Sesi Habis

## Prerequisites

- Mode: FE+BE (backend nyata).
- Spec ini kelas blokir karena kondisi data (prinsip 12 bagian 3): opsi mandiri nonaktif (Client NoByo) dan pool kuota sesi habis (Client Quota).
- Akun (dua client; akun pertama di hook `before`, ganti akun eksplisit di langkah 8):
  - Total Control Client NoByo `totalControl_automated_qaNoByo@qwertysystem.net` (Eka Pratama), `Spectra.env.GS_TC_NOBYO_PASSWORD`; opsi mandiri nonaktif; tidak ada stok resmi untuk IMEI `356938035643101`.
  - Total Control Client Quota `totalControl_automated_qaQuota@qwertysystem.net` (Fitri Handayani), `Spectra.env.GS_TC_QUOTA_PASSWORD`; plan Growth; opsi mandiri aktif; GPS kuota 3 dengan terpakai 1 (sisa 2) disetel fixture BE di langkah 9.
  - Nama env `GS_TC_NOBYO_PASSWORD` dan `GS_TC_QUOTA_PASSWORD` belum terdaftar di `spectra.config.ts` dan `.env.example` (lihat `suite.md` bagian Kredensial). Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A).
- Layar awal Global Settings > TAG > Tab All dibuka hook `beforeEach` untuk akun pertama; setelah ganti akun dibuka di langkah ganti akun.
- State yang diubah: jumlah terpakai kuota GPS Client Quota; hook `after` memulihkannya ke nilai awal (dicatat di hook `before`).
- Kemampuan teknis: entri manual GPS (input teks dan tombol `Add`; label dan placeholder kontrol menunggu desain, NC-11, selektor disediakan tim FE, S-13) dan unggah berkas CSV/XLSX; tidak ada endpoint atau selektor yang dikarang spec ini.
- Spec tidak melakukan Submit Activation; registri Client A tidak berubah.
- Suite serial (`parallel: false`); spec tidak bergantung pada hasil spec lain. Identifier TAG (EPC, IMEI, UID) tetap dan tidak dapat diberi sufiks `{runId}` (S-12), sehingga seeding bersifat idempotent: hook `before` mengembalikan data yang dipakai spec ini ke kondisi awal (Q-4).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya; lihat `suite.md` bagian Hook Guided Tooltip.
- Nilai data mengacu ke `fixtures/all-tags.json` (identitas saja, dibuat tahap script); tidak ada password di fixture.

## Test Steps

### TC-GS-TAG-63: Opsi mandiri nonaktif menghasilkan Error T-10

1. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
2. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643101`
3. Hover lencana `Error` baris `356938035643101`
4. Verifikasi baris `356938035643101` berstatus `Error`
5. Verifikasi tooltip `Not in your official stock; self-purchased activation is not enabled for your account. Contact your administrator.`
6. Verifikasi aksi baris `356938035643101` hanya `Remove` (baris tidak bisa di-resolve)
7. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog `Unsaved Changes` (staging berisi baris)
8. Ganti akun: logout, login sebagai Total Control Client Quota (`Spectra.env.GS_TC_QUOTA_PASSWORD`)
9. Setel GPS Client Quota kuota 3 dengan terpakai 1 (sisa 2) lewat fixture BE (disediakan tim FE/BE)
10. Buka Global Settings > TAG > Tab All

### TC-GS-TAG-64: Pool sesi habis menghasilkan Error T-11

11. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
12. Buka section `Self-Purchased Template`
13. Isi Template Device Name `Queclink GV300` dan Brand `Queclink`
14. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643101` lalu `356938035643102` lalu `356938035643103` berurutan
15. Hover lencana `Error` baris `356938035643103`
16. Verifikasi baris `356938035643101` dan `356938035643102` berstatus `Self-Purchased`
17. Verifikasi baris `356938035643103` berstatus `Error`
18. Verifikasi tooltip lencana `Error` baris `356938035643103` adalah `License limit reached.`
19. Verifikasi input entri manual dan tombol `Add` tetap aktif setelah baris `Error` (sesi entri tidak berhenti)
20. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog `Unsaved Changes` (staging berisi baris)

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Kelas harness: blokir karena kondisi data (prinsip 12 bagian 3) dengan data kuota disetel fixture BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memakai dua client dengan Step ganti akun eksplisit (langkah 8); bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (pemisah akun kasus b, bagian 3).
- Langkah penghubung (tanpa `Verifikasi`): langkah mulai sesi menggabungkan TC langkah 1 sampai 3; hover lencana `Error` adalah pengamatan tooltip; langkah 9 menyiapkan Precondition TC-64; `Buka section` dan isi Template menjalankan TC-64 langkah 4; `Kembali ke List` dengan `Leave` adalah langkah penghubung (S-03) karena dialog `Unsaved Changes` muncul pada sesi dengan baris staging, sedangkan definisi dirty dan teks dialog diuji di spec 036 (TC-183 sampai TC-185, TC-111 sampai TC-113) dan tidak diasersi di spec ini.
- Temuan untuk QA:
  - TC-64 Expected b ("Sesi entri tidak berhenti; baris `Error` tidak mengurangi pool") tidak punya ukuran teramati; spec mengasersi input dan `Add` tetap aktif, sedangkan "tidak mengurangi pool" tidak diasersi karena TC tidak menyebut indikator pool selain kartu kuota.
  - TC-63 Expected b ("baris tidak bisa di-resolve") sama dengan aksi baris hanya `Remove`; satu `Verifikasi` (langkah 6).
  - TC-64 Pre-setup menyebut "kuota 3 terpakai 1 (sisa 2)"; TC-41 memakai terpakai 2 pada client yang sama, sehingga fixture BE perlu mengatur nilai per spec (Q-4).
