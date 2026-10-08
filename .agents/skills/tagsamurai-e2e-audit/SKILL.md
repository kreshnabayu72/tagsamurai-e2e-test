---
name: tagsamurai-e2e-audit
description: Audit hasil generate e2e TAG Samurai untuk satu suite: traceability TC granular → spec.md → web.test.ts, kepatuhan konvensi efisiensi dan data. Hanya melaporkan temuan, tidak memperbaiki.
---

# Audit E2E (report-only)

Skill ini hanya **melaporkan**. Jangan mengubah file apa pun, termasuk spec, script, dan TC granular. Tampilkan temuan ke user dan tunggu instruksi. Jangan langsung memperbaiki walau temuannya jelas.

Rujukan aturan: `docs/e2e-conventions.md`. Skill ini melengkapi `spectra lint`, yang hanya memeriksa format. Jalankan `spectra lint --strict specs/<Suite>` dan `pnpm type-check` dulu, lalu periksa hal-hal yang tidak dicakup linter.

## Input

Path suite (contoh `specs/GlobalSettings/User`) dan path `tc-[modul].md` sumbernya.

## Pemeriksaan

**A. Traceability (arah TC granular → spec)**
- Ekstrak semua id TC di `tc-[modul].md`. Untuk tiap id: apakah muncul di `sourceTc` spec mana pun, atau tercatat di `docs/coverage/<Suite>.md` sebagai TC hanya-BE (dengan id TC BE bila ada)?
- Satu-satunya alasan sah sebuah TC tidak punya spec adalah hanya-BE. Alasan lain, termasuk "sudah dicakup FE", "tidak layak", "butuh waktu/kuota/race/mock", atau label "Manual", adalah temuan.
- Spec hanya-FE harus punya baris `Mode: mock` di `## Prerequisites` beserta kebutuhan mock-nya (endpoint dan respons yang dipaksa).
- Cek Changelog `tc-[modul].md` sebelum menyimpulkan ada id yang hilang (id yang sudah dihapus resmi bukan temuan).

**B. Traceability (arah spec → TC granular)**
- Setiap `sourceTc` menunjuk id yang benar-benar ada di `tc-[modul].md`.
- Isi spec sesuai TC sumbernya (role, precondition, langkah, expected result). Bandingkan per TC yang digabung. Langkah atau expected result yang hilang, ditambah, atau berubah makna adalah temuan.
- `priority` sesuai mapping bagian 8 konvensi (tertinggi dari TC sumber).
- `caseType` mengikuti aturan spec gabungan bagian 8 konvensi (jenis alur utama yang dominan). Jangan menandai temuan hanya karena TC sumber campuran jenisnya.
- Label tombol dan cara menutup form sesuai bagian 9 konvensi (Create `[Submit]`, Edit `[Save]`, `[Clear Field]`, `✕`/`Esc`, tanpa `[Cancel]` pada modal). Cocokkan ke `prd-conventions.md` §24.1, bukan hanya ke TC.
- `coverage.web` tidak dinilai terhadap `status`. Kolom itu hanya jenis pengujian, progres dibaca dari `status`.
- Bahasa spec Indonesia (bagian 7 konvensi): narasi Indonesia, teks UI persis seperti di aplikasi, langkah asersi diawali `Verifikasi`. Spec berbahasa Inggris adalah temuan.
- Spec Role Matrix (bagian 3a): dipisah positif dan negatif, ada tabel "Role yang diuji", dan tiap kombinasi role × aksi punya TC granular sumber. Kombinasi tanpa TC sumber adalah temuan.

**C. Spec → script**
- Tiap langkah `Verifikasi ...` di spec.md punya assertion di `web.test.ts`, dan urutannya sama.
- Script tidak berisi aksi atau assertion yang tidak ada di spec.md.
- `it()` title = `title`. `@step` = `Step.*` (linter sudah memeriksa, konfirmasi hasilnya).
- Assertion tidak dangkal: bukan hanya cek elemen ada padahal expected result menyebut isi, badge, atau toast tertentu.

**D. Efisiensi dan independensi**
- Spec tidak bergantung pada data atau hasil spec lain (cari nama data yang dibuat di spec lain).
- Login dan seed dilakukan di hook, bukan diulang di tiap `it()`.
- Jumlah buka form/modal per spec tidak lebih dari jumlah kejadian yang menutup form. Tandai spec yang membuka form ulang tanpa alasan.
- Screening ada di awal spec. Validasi yang diblokir ada sebelum aksi sukses. Kasus menutup form ada di akhir.
- Tidak ada dua spec dengan alur dan assert yang sama, dan tidak ada spec yang seharusnya digabung (topik sama, bisa satu alur) tetapi terpisah. Sebaliknya, topik aksi berbeda dengan kondisi data bervariasi (Delete, Toggle Active, Remove Access) yang tergabung dalam satu spec adalah temuan.
- Aksi yang menghapus data ada di akhir spec. Spec yang memakai Select All lalu Bulk Delete tidak berjalan paralel dan tidak mendahului spec lain.
- Spec tidak mencampur role atau entity berbeda tanpa Step ganti akun, kecuali spec Role Matrix.
- Setup yang dibutuhkan satu spec tidak ditaruh di `global-hooks`.
- Spec yang membuat data punya cleanup, dan spec tanpa pembuatan data tidak menumpang data spec lain.

**E. Data**
- Tidak ada password, token, atau kredensial di spec, fixture, atau script.
- Data yang harus unik memakai suffix dinamis. Data yang dibuat spec dibersihkan di hook.
- Setiap data, akun, kondisi environment, dan kemampuan teknis yang dipakai langkah spec tercantum di `## Prerequisites`, bukan hanya di `## Notes`.
- Data pre-setup mengacu ke fixture yang cocok dengan tabel Data Uji Pre-setup di TC sumber.

**F. Kode**
- Tidak ada selector mentah di `web.test.ts`. Tidak ada xpath atau nth-child di Page Object.
- Tidak ada `sleep` atau jeda tetap, komentar di kode, import manual, atau `describe`/`test`.
- Struktur: suite di `specs/<ModulBesar>/<SubModul>/`, nama folder TC = id, penamaan entitas berprefix modul, tidak ada file di luar folder standar.

## Format laporan

1. Ringkasan: jumlah TC granular, jumlah spec, TC diotomasi / dilewati / belum tercakup, hasil lint dan type-check.
2. Tabel temuan, diurutkan dari yang paling berat: `No` | `Kategori (A-F)` | `Spec/TC` | `Temuan` | `Bukti (file:baris)` | `Penyebab (1/2)` | `Rekomendasi` | `Diubah di`.
   - `Rekomendasi`: perubahan konkret yang menutup temuan (apa yang ditulis, dipindah, atau dihapus), bukan sekadar "perbaiki".
   - `Diubah di`: file yang harus diedit, salah satu atau lebih dari `spec` (spec.md suite), `TC` (`tc-[modul].md`), `PRD` (PRD modul), `konvensi` (`docs/e2e-conventions.md`), `skill generator` (`tagsamurai-e2e-generate-spec`), `coverage` (`docs/coverage/<Suite>.md`). Temuan penyebab (2) tidak boleh hanya `spec`. Temuan penyebab (1) yang berulang di beberapa spec juga mencantumkan `skill generator` supaya tidak terulang.
3. Bagian "Perlu keputusan" untuk hal yang tidak bisa disimpulkan dari file (contoh: TC sumber ambigu, atau selector belum ada di app). Tiap butir memuat opsi beserta rekomendasi pilihan dan alasannya.
4. Bagian "Rekomendasi urutan perbaikan": kelompokkan temuan per file tujuan (`TC`/`PRD`/`konvensi` dulu karena sumber, lalu `skill generator`, lalu `spec`/`coverage`), dan sebut workflow yang dipakai (contoh `audit-testcase` untuk TC, `e2e-generate-spec` untuk spec).

Bedakan dua jenis penyebab pada tiap temuan: (1) kesalahan hasil generate, atau (2) kekurangan di TC sumber atau konvensi. Untuk jenis (2) arahkan ke perbaikan sumber, jangan ke spec.
